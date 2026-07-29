from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AgentProfile:
    """
    Defines an AI agent personality.
    """

    name: str

    role: str

    expertise: str

    system_prompt: str
