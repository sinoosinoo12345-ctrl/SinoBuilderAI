from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class UniversalContext:

    request: str

    project_type: str = "unknown"

    platforms: list[str] = field(default_factory=list)

    technologies: list[str] = field(default_factory=list)

    modules: list[str] = field(default_factory=list)

    ui_style: str = "modern"

    database: str = ""

    ai_required: bool = False


class UniversalAnalyzer:

    """
    Universal Project Analyzer.

    Understands any application request and
    extracts the project structure.
    """

    def analyze(
        self,
        request: str,
    ) -> UniversalContext:

        text = request.lower()

        context = UniversalContext(
            request=request,
        )

        if "ذكاء" in text or "ai" in text:
            context.ai_required = True

        if "flutter" in text or "android" in text or "ios" in text:
            context.platforms.append("flutter")

        if "ويب" in text or "web" in text:
            context.platforms.append("web")

        if not context.platforms:
            context.platforms.extend([
                "flutter",
                "web",
            ])

        context.technologies.extend([
            "FastAPI",
            "Flutter",
            "SQLite",
        ])

        context.database = "SQLite"

        context.ui_style = "Modern Glass"

        return context
