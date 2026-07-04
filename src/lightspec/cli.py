from pathlib import Path
from typing import Optional

import typer

from .filesystem import ensure_existing_directory, ensure_project_directory
from .installer import install_project_assets
from .models import Agent
from .prompts import resolve_agent
from .version import __version__

app = typer.Typer(help="LightSpec CLI")


@app.command("version")
def version() -> None:
    """Print the installed LightSpec CLI version."""
    typer.echo(__version__)


@app.command("init")
def init(
    project_name: str,
    agent: Optional[Agent] = typer.Option(None, "--agent", help="Coding agent integration."),
    path: Optional[Path] = typer.Option(None, "--path", help="Base path where the project folder will be created."),
    non_interactive: bool = typer.Option(False, "--non-interactive", help="Use defaults instead of prompting."),
    force: bool = typer.Option(False, "--force", help="Allow initialization inside an existing directory."),
) -> None:
    """Create a new LightSpec project scaffold."""
    selected_agent = resolve_agent(agent, non_interactive)
    project_root = ensure_project_directory(project_name, path, force)
    summary = install_project_assets(project_root, selected_agent, __version__, force=force)

    typer.echo(f"LightSpec project created at: {project_root}")
    typer.echo(f"Agent integration: {selected_agent.value}")
    typer.echo(f"Common files copied: {summary.common_files}")
    typer.echo(f"Skills copied: {summary.skill_count}")


@app.command("install")
def install(
    agent: Optional[Agent] = typer.Option(None, "--agent", help="Coding agent integration."),
    path: Optional[Path] = typer.Option(None, "--path", help="Existing project path. Defaults to the current directory."),
    non_interactive: bool = typer.Option(False, "--non-interactive", help="Use defaults instead of prompting."),
    force: bool = typer.Option(False, "--force", help="Overwrite existing LightSpec-managed files and folders."),
) -> None:
    """Install LightSpec into an existing project directory."""
    selected_agent = resolve_agent(agent, non_interactive)
    project_root = ensure_existing_directory(path)
    summary = install_project_assets(project_root, selected_agent, __version__, force=force)

    typer.echo(f"LightSpec installed in: {project_root}")
    typer.echo(f"Agent integration: {selected_agent.value}")
    typer.echo(f"Common files copied: {summary.common_files}")
    typer.echo(f"Skills copied: {summary.skill_count}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
