from enum import Enum
from typing import TypeVar

import questionary
import typer

from .models import Agent


EnumChoice = TypeVar("EnumChoice", bound=Enum)


def _prompt_enum(prompt_label: str, enum_type: type[EnumChoice]) -> EnumChoice:
    choices = [
        questionary.Choice(title=item.value, value=item)
        for item in enum_type
    ]

    result = questionary.select(
        f"{prompt_label}\nUse ↑/↓ to move and Enter to confirm.",
        choices=choices,
    ).ask()

    if result is None:
        raise typer.Abort()

    return result


def resolve_agent(agent: Agent | None, non_interactive: bool) -> Agent:
    if agent is not None:
        return agent
    if non_interactive:
        return Agent.COPILOT
    return _prompt_enum("Choose the coding agent", Agent)
