from __future__ import annotations

from ai.core.file_manifest import FileManifest
from ai.core.architecture_context import ArchitectureContext


class ManifestBuilder:
    """
    Sino Builder AI
    Universal Project Manifest Generator.

    Converts architecture decisions
    into complete project structure.
    """


    def build(
        self,
        architecture: ArchitectureContext,
    ) -> FileManifest:

        manifest = FileManifest()


        core_files = [

            (
                "README.md",
                "Project documentation",
            ),

            (
                "backend/main.py",
                "Backend application entry point",
            ),

            (
                "database/models.py",
                "Database entities and models",
            ),

            (
                "frontend/main.py",
                "Frontend application entry",
            ),

            (
                "config/settings.py",
                "Application configuration",
            ),

        ]


        for path, description in core_files:

            manifest.add(
                path,
                description,
            )


        if "ai" in architecture.layers:

            manifest.add(
                "ai/core_engine.py",
                "Artificial Intelligence engine",
            )


        if "backend" in architecture.layers:

            manifest.add(
                "backend/api.py",
                "API routing layer",
            )


        if "database" in architecture.layers:

            manifest.add(
                "database/database.py",
                "Database connection",
            )


        if "frontend" in architecture.layers:

            manifest.add(
                "frontend/screens/home.py",
                "Main application screen",
            )


        for module in architecture.modules:

            name = module.lower()


            if name in (
                "authentication",
                "auth",
                "users",
            ):

                manifest.add(
                    "backend/auth.py",
                    "Authentication system",
                )


            elif name in (
                "market_data",
                "data",
            ):

                manifest.add(
                    "backend/data_service.py",
                    "Data processing service",
                )


            elif name in (
                "charts",
                "chart",
            ):

                manifest.add(
                    "frontend/screens/chart.py",
                    "Professional chart screen",
                )


            elif name == "portfolio":

                manifest.add(
                    "frontend/screens/portfolio.py",
                    "Portfolio screen",
                )


            elif name == "orders":

                manifest.add(
                    "backend/orders.py",
                    "Orders management",
                )


            elif name in (
                "payments",
                "billing",
            ):

                manifest.add(
                    "backend/payment.py",
                    "Payment processing",
                )


            elif name == "signals":

                manifest.add(
                    "backend/signals.py",
                    "AI signals engine",
                )


            elif name in (
                "risk_management",
                "risk",
            ):

                manifest.add(
                    "backend/risk_management.py",
                    "Risk management",
                )


            elif name == "trading_agent":

                manifest.add(
                    "ai/trading_agent.py",
                    "AI trading analysis engine",
                )


            else:

                manifest.add(
                    f"backend/{name}.py",
                    f"{module} service module",
               )


        return manifest
