import json
from dataclasses import dataclass
from importlib.resources import files
from pathlib import Path

from .integrations import INTEGRATION_TARGETS
from .models import Agent


@dataclass(frozen=True)
class InstallSummary:
    common_files: int
    skill_count: int


def _managed_paths(project_root: Path, agent: Agent) -> list[Path]:
    target_root = project_root / INTEGRATION_TARGETS[agent].root_dir / "skills"

    paths = [
        project_root / "constitution.md",
        project_root / "code_standards.md",
        project_root / "workflow_rules.md",
        target_root,
        project_root / ".lightspec" / "project.json",
    ]
    return paths


def _validate_install_destination(project_root: Path, agent: Agent, force: bool) -> None:
    conflicts = [path for path in _managed_paths(project_root, agent) if path.exists()]
    if conflicts and not force:
        formatted = "\n".join(str(path) for path in conflicts)
        raise ValueError(
            "LightSpec-managed files or folders already exist at the destination. "
            "Use --force to overwrite them.\n"
            f"{formatted}"
        )


def _copy_tree(source, destination: Path) -> int:
    count = 0
    if source.is_dir():
        destination.mkdir(parents=True, exist_ok=True)
        for child in source.iterdir():
            count += _copy_tree(child, destination / child.name)
        return count

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(source.read_bytes())
    return 1


def _write_metadata(project_root: Path, agent: Agent, version: str) -> None:
    metadata_path = project_root / ".lightspec" / "project.json"
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    metadata_path.write_text(
        json.dumps(
            {
                "name": project_root.name,
                "agent": agent.value,
                "lightspec_version": version,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def install_project_assets(project_root: Path, agent: Agent, version: str, force: bool = False) -> InstallSummary:
    asset_root = files("lightspec") / "assets"
    _validate_install_destination(project_root, agent, force)

    common_root = asset_root / "common"
    common_files = 0
    for item in common_root.iterdir():
        common_files += _copy_tree(item, project_root / item.name)

    target_root = project_root / INTEGRATION_TARGETS[agent].root_dir / "skills"
    skills_root = asset_root / "skills"
    skill_count = 0
    for item in skills_root.iterdir():
        skill_count += _copy_tree(item, target_root / item.name)

    _write_metadata(project_root, agent, version)
    return InstallSummary(common_files=common_files, skill_count=skill_count)
