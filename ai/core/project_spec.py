from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class UniversalProjectSpec:

    name: str

    description: str

    goal: str

    architecture: Dict = field(default_factory=dict)

    frontend: List[str] = field(default_factory=list)

    backend: List[str] = field(default_factory=list)

    database: List[str] = field(default_factory=list)

    api: List[str] = field(default_factory=list)

    ai_modules: List[str] = field(default_factory=list)

    agents: List[str] = field(default_factory=list)

    security: List[str] = field(default_factory=list)

    deployment: Dict = field(default_factory=dict)

    metadata: Dict = field(default_factory=dict)
