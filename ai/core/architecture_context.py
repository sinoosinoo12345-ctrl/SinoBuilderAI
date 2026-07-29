from __future__ import annotations

from dataclasses import dataclass, field



@dataclass
class ArchitectureContext:
    """
    Stores system architecture decisions.
    """


    project_type: str = ""


    description: str = ""


    layers: list[str] = field(
        default_factory=list
    )


    modules: list[str] = field(
        default_factory=list
    )


    technologies: list[str] = field(
        default_factory=list
    )


    decisions: list[str] = field(
        default_factory=list
    )


    def add_decision(
        self,
        decision: str,
    ):

        self.decisions.append(
            decision
        )



    def summary(self) -> dict:

        return {

            "project_type": self.project_type,

            "layers": self.layers,

            "modules": self.modules,

            "technologies": self.technologies,

            "decisions": self.decisions,

        }
