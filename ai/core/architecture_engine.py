from __future__ import annotations

from ai.core.architecture_context import ArchitectureContext
from ai.core.requirement_engine import RequirementEngine


class ArchitectureEngine:
    """
    Universal Architecture Intelligence Engine.
    Detects project domain and builds architecture.
    """

    def __init__(self):

        self.requirements = RequirementEngine()


    def analyze(
        self,
        project_name: str,
        requirements: str,
    ) -> ArchitectureContext:


        analysis = self.requirements.analyze(
            requirements
        )


        text = requirements.lower()


        context = ArchitectureContext(
            project_type=analysis.project_type,
            description=requirements,
        )


        # Base Architecture

        context.layers.extend(
            [
                "frontend",
                "backend",
                "database",
            ]
        )


        if (
            "ai" in text
            or "ذكاء" in text
            or "ذكي" in text
            or "AI Engine" in analysis.technologies
        ):

            context.layers.append(
                "ai"
            )


        context.technologies.extend(
            [
                "FastAPI",
                "Flutter",
                "SQLite",
            ]
        )


        # Authentication always

        context.modules.append(
            "authentication"
        )


        # =========================
        # Domain Detection
        # =========================


        domains = {


            "trading": [
                "market_data",
                "charts",
                "portfolio",
                "signals",
                "risk_management",
            ],


            "medical": [
                "patients",
                "appointments",
                "medical_records",
                "reports",
            ],


            "shop": [
                "products",
                "orders",
                "cart",
                "payments",
            ],


            "education": [
                "courses",
                "students",
                "lessons",
                "exams",
            ],


            "social": [
                "users",
                "posts",
                "messages",
                "notifications",
            ],


            "management": [
                "users",
                "reports",
                "dashboard",
                "analytics",
            ],

        }


        for domain, modules in domains.items():

            keywords = {

                "trading": [
                    "تداول",
                    "trading",
                    "mt5",
                ],

                "medical": [
                    "مستشفى",
                    "طب",
                    "medical",
                    "health",
                ],

                "shop": [
                    "متجر",
                    "بيع",
                    "shop",
                    "store",
                ],

                "education": [
                    "تعليم",
                    "مدرسة",
                    "course",
                ],

                "social": [
                    "اجتماعي",
                    "social",
                ],

                "management": [
                    "ادارة",
                    "management",
                ],

            }


            if any(
                word in text
                for word in keywords[domain]
            ):

                context.project_type = domain

                for module in modules:

                    if module not in context.modules:

                        context.modules.append(
                            module
                        )


                context.add_decision(
                    f"Detected domain: {domain}"
                )


                break


        # Add requirement features

        for feature in analysis.features:

            if feature not in context.modules:

                context.modules.append(
                    feature
                )


        context.add_decision(
            "Use Clean Architecture"
        )

        context.add_decision(
            "Generate scalable modular system"
        )


        if "ai" in context.layers:

            context.add_decision(
                "Integrate AI intelligence layer"
            )


        return context
