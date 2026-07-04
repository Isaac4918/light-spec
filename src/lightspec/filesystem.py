from pathlib import Path

import typer


def ensure_project_directory(project_name: str, base_path: Path | None, force: bool) -> Path:
    if not project_name or project_name in {".", ".."}:
        raise typer.BadParameter("Project name must be a valid folder name.")

    if Path(project_name).name != project_name:
        raise typer.BadParameter("Project name must not include path separators.")

    root = (base_path or Path.cwd()).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    target = root / project_name

    if target.exists() and target.is_file():
        raise typer.BadParameter(f"Destination exists as a file: {target}")

    if target.exists() and any(target.iterdir()) and not force:
        raise typer.BadParameter(
            f"Destination directory already exists and is not empty: {target}. Use --force to continue."
        )

    target.mkdir(parents=True, exist_ok=True)
    return target


def ensure_existing_directory(path: Path | None) -> Path:
    target = (path or Path.cwd()).expanduser().resolve()

    if not target.exists():
        raise typer.BadParameter(f"Destination directory does not exist: {target}")

    if not target.is_dir():
        raise typer.BadParameter(f"Destination is not a directory: {target}")

    return target
