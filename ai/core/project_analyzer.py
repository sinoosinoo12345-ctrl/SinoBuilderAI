from dataclasses import dataclass, asdict
import re


@dataclass
class ProjectSpec:

    name: str

    description: str

    project_type: str

    pages: list

    entities: list

    services: list

    ai_required: bool

    auth_required: bool

    database_required: bool


class ProjectAnalyzer:

    def analyze(self, description: str):

        text = description.lower()

        pages = []

        entities = []

        services = []

        ai_required = False

        auth_required = True

        database_required = True

        if "ذكاء" in description or "ai" in text:
            ai_required = True

        keywords = re.findall(r"[A-Za-z\u0600-\u06FF]+", description)

        for word in keywords:

            if len(word) > 3:

                entities.append(word)

        if "تسجيل" in description:
            pages.append("Login")

        if "لوحة" in description:
            pages.append("Dashboard")

        if "ادارة" in description:
            pages.append("Management")

        if not pages:
            pages = [
                "Home",
                "Dashboard",
                "Settings"
            ]

        services = [
            "Frontend",
            "Backend",
            "Database"
        ]

        if ai_required:
            services.append("AI Engine")

        return ProjectSpec(

            name="GeneratedProject",

            description=description,

            project_type="Universal",

            pages=pages,

            entities=entities,

            services=services,

            ai_required=ai_required,

            auth_required=auth_required,

            database_required=database_required

        )

    def export(self, spec):

        return asdict(spec)
