from __future__ import annotations

from dataclasses import dataclass, field



@dataclass
class AgentMemoryBus:
    """
    Shared communication memory
    between AI agents.
    """

    plans: list[str] = field(
        default_factory=list
    )

    decisions: list[str] = field(
        default_factory=list
    )

    architecture_notes: list[str] = field(
        default_factory=list
    )

    generated_files: list[str] = field(
        default_factory=list
    )

    warnings: list[str] = field(
        default_factory=list
    )



    def add_plan(
        self,
        plan: str,
    ):

        self.plans.append(
            plan
        )



    def add_decision(
        self,
        decision: str,
    ):

        self.decisions.append(
            decision
        )



    def add_architecture_note(
        self,
        note: str,
    ):

        self.architecture_notes.append(
            note
        )



    def add_file(
        self,
        file: str,
    ):

        self.generated_files.append(
            file
        )



    def add_warning(
        self,
        warning: str,
    ):

        self.warnings.append(
            warning
        )



    def snapshot(self) -> dict:

        return {

            "plans": self.plans,

            "decisions": self.decisions,

            "architecture_notes": self.architecture_notes,

            "generated_files": self.generated_files,

            "warnings": self.warnings,

        }
