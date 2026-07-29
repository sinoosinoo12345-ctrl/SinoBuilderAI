from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class RequirementContext:

    original_prompt: str

    project_type: str = "general"

    platforms: list[str] = field(
        default_factory=list
    )

    technologies: list[str] = field(
        default_factory=list
    )

    features: list[str] = field(
        default_factory=list
    )


class RequirementEngine:
    """
    Sino Builder AI
    Universal Requirement Analyzer
    """


    def analyze(
        self,
        prompt: str,
    ) -> RequirementContext:


        text = prompt.lower()


        ctx = RequirementContext(
            original_prompt=prompt
        )


        # ======================
        # Domain Detection
        # ======================

        domains = {

            "trading": [
                "تداول",
                "trading",
                "forex",
                "crypto",
                "mt5",
            ],

            "medical": [
                "مستشفى",
                "طب",
                "medical",
                "health",
                "doctor",
            ],

            "ecommerce": [
                "متجر",
                "shop",
                "store",
                "ecommerce",
                "بيع",
            ],

            "education": [
                "تعليم",
                "school",
                "course",
                "جامعة",
            ],

            "social": [
                "اجتماعي",
                "social",
                "chat",
            ],

            "ai_platform": [
                "ذكاء اصطناعي",
                "artificial intelligence",
                "ai",
            ],

        }


        for domain, words in domains.items():

            if any(
                word in text
                for word in words
            ):

                ctx.project_type = domain
                break


        # ======================
        # Platforms
        # ======================


        if any(
            k in text
            for k in [
                "android",
                "ios",
                "flutter",
                "موبايل",
            ]
        ):

            ctx.platforms.append(
                "flutter"
            )


        if any(
            k in text
            for k in [
                "web",
                "ويب",
                "website",
                "react",
            ]
        ):

            ctx.platforms.append(
                "web"
            )


        if not ctx.platforms:

            ctx.platforms.extend(
                [
                    "flutter",
                    "web",
                ]
            )


        # ======================
        # Technologies
        # ======================

        ctx.technologies.extend(
            [
                "FastAPI",
                "SQLite",
            ]
        )


        if (
            "ai" in text
            or "ذكاء" in text
        ):

            ctx.technologies.append(
                "AI Engine"
            )


        # ======================
        # Universal Features
        # ======================

        universal_features = [

            ("authentication", [
                "login",
                "تسجيل",
                "حساب",
            ]),

            ("dashboard", [
                "لوحة",
                "dashboard",
            ]),

            ("notifications", [
                "اشعارات",
                "notifications",
            ]),

            ("chat", [
                "chat",
                "دردشة",
            ]),

        ]


        for feature, words in universal_features:

            if any(
                w in text
                for w in words
            ):

                ctx.features.append(
                    feature
                )


        # ======================
        # Domain Features
        # ======================

        domain_features = {

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

            "ecommerce": [
                "products",
                "cart",
                "orders",
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
            ],

        }


        for feature in domain_features.get(
            ctx.project_type,
            []
        ):

            if feature not in ctx.features:

                ctx.features.append(
                    feature
                )


        return ctx
