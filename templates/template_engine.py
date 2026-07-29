from dataclasses import dataclass, asdict


@dataclass
class ProjectSpec:
    title: str
    description: str
    modules: list
    entities: list
    pages: list
    apis: list
    database: bool
    authentication: bool
    ai_features: bool


class ProjectAnalyzer:

    def analyze(self, description: str):

        return ProjectSpec(
            title="Generated Project",
            description=description,
            modules=[],
            entities=[],
            pages=[],
            apis=[],
            database=True,
            authentication=True,
            ai_features=("ai" in description.lower() or "ذكاء" in description)
        )

    def to_dict(self, spec: ProjectSpec):
        return asdict(spec)
