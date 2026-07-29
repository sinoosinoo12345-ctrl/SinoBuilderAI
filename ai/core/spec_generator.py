from __future__ import annotations

from ai.core.specification import (
    Feature,
    Screen,
    Specification,
)

from ai.core.requirement_engine import (
    RequirementEngine,
)


class SpecificationGenerator:
    """
    Sino Builder AI
    Universal Specification Generator
    """

    def __init__(self):

        self.requirements = RequirementEngine()


    def generate(
        self,
        prompt: str,
    ) -> Specification:

        analysis = self.requirements.analyze(
            prompt
        )

        spec = Specification(

            title=prompt,

            description=prompt,

            platforms=analysis.platforms.copy(),

        )

        # -----------------------------
        # Trading
        # -----------------------------

        if analysis.project_type == "trading":

            spec.screens.extend([

                Screen(
                    "Splash",
                    "Application startup",
                ),

                Screen(
                    "Login",
                    "Authentication",
                ),

                Screen(
                    "Home",
                    "Trading Dashboard",
                ),

                Screen(
                    "Chart",
                    "Professional Trading Chart",
                ),

                Screen(
                    "Portfolio",
                    "Open Positions",
                ),

                Screen(
                    "Signals",
                    "AI Signals",
                ),

                Screen(
                    "Settings",
                    "Application Settings",
                ),

            ])

            spec.features.extend([

                Feature(
                    "Authentication",
                    "Secure login",
                ),

                Feature(
                    "Market Data",
                    "Real time prices",
                ),

                Feature(
                    "Charts",
                    "Candlestick Charts",
                ),

                Feature(
                    "Portfolio",
                    "Trading Portfolio",
                ),

                Feature(
                    "AI Analysis",
                    "Market Intelligence",
                ),

                Feature(
                    "Risk Management",
                    "Capital Protection",
                ),

            ])

            spec.database.extend([

                "users",
                "orders",
                "positions",
                "signals",

            ])

            spec.apis.extend([

                "/login",
                "/market",
                "/portfolio",
                "/signals",

            ])

        # -----------------------------
        # Default
        # -----------------------------

        else:

            spec.screens.extend([

                Screen(
                    "Splash",
                    "Startup",
                ),

                Screen(
                    "Home",
                    "Dashboard",
                ),

                Screen(
                    "Settings",
                    "Settings",
                ),

            ])

            spec.features.extend([

                Feature(
                    "Authentication",
                    "Secure Login",
                ),

                Feature(
                    "Localization",
                    "Arabic & English",
                ),

            ])

            spec.database.extend([

                "users",

            ])

            spec.apis.extend([

                "/login",

            ])

        return spec
