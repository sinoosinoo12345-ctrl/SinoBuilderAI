from __future__ import annotations

from pathlib import Path

from app.application import SinoBuilderApplication


class SystemCheck:
    """
    Sino Builder AI
    System Check
    Release V1
    """

    REQUIRED = [

        "ai",

        "builder",

        "template_engine",

        "plugin_sdk",

        "integration",

        "release",

        "app",

    ]

    def run(
        self,
    ) -> dict:

        errors = []

        root = Path(".")

        for folder in self.REQUIRED:

            if not (
                root / folder
            ).exists():

                errors.append(
                    f"Missing: {folder}"
                )

        try:

            application = (
                SinoBuilderApplication()
            )

            status = (
                application.status()
            )

        except Exception as error:

            errors.append(
                str(error)
            )

            status = {}

        return {

            "status":
                "ready"
                if not errors
                else "failed",

            "errors":
                errors,

            "application":
                status,

        }


if __name__ == "__main__":

    result = SystemCheck().run()

    print(result)
