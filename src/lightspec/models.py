from dataclasses import dataclass
from enum import Enum


class Agent(str, Enum):
    COPILOT = "copilot"
    CLAUDE = "claude"
    OPENCODE = "opencode"


@dataclass(frozen=True)
class IntegrationTarget:
    root_dir: str
