from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class AgentContext:
    """
    Universal shared context for Sino Builder AI.
    """

    request: str

    project: str = ""

    project_type: str = ""

    architecture: object | None = None

    specification: dict = field(default_factory=dict)

    manifest: list[str] = field(default_factory=list)

    technologies: list[str] = field(default_factory=list)

    layers: list[str] = field(default_factory=list)

    modules: list[str] = field(default_factory=list)

    affected_files: list[str] = field(default_factory=list)

    generated_files: list[str] = field(default_factory=list)

    decisions: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    # --------------------

    def add_decision(self, decision: str):
        self.decisions.append(decision)

    def add_warning(self, warning: str):
        self.warnings.append(warning)

    def add_error(self, error: str):
        self.errors.append(error)

    def add_generated_file(self, file: str):
        if file not in self.generated_files:
            self.generated_files.append(file)

    def add_affected_file(self, file: str):
        if file not in self.affected_files:
            self.affected_files.append(file)

    def add_manifest_file(self, file: str):
        if file not in self.manifest:
            self.manifest.append(file)

    def add_agent_result(
        self,
        agent_name: str,
        result,
    ):
        self.metadata[agent_name] = result

    def get_agent_result(
        self,
        agent_name: str,
    ):
        return self.metadata.get(agent_name)

    def set_architecture(self, architecture: dict):
        self.architecture = architecture

    def set_specification(self, specification: dict):
        self.specification = specification
