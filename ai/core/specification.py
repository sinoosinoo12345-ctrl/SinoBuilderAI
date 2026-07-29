from dataclasses import dataclass, field


@dataclass(slots=True)
class Screen:
    name: str
    description: str
    title: str = ""


@dataclass(slots=True)
class Feature:

    name: str
    description: str


@dataclass(slots=True)
class Specification:

    title: str

    description: str

    platforms: list[str] = field(default_factory=list)

    screens: list[Screen] = field(default_factory=list)

    features: list[Feature] = field(default_factory=list)

    database: list[str] = field(default_factory=list)

    apis: list[str] = field(default_factory=list)
