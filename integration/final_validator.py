from __future__ import annotations

from pathlib import Path


class FinalValidator:
    """
    Sino Builder AI
    Smart Final Validator
    Release V2
    """

    REQUIRED = {
    "frontend": [
        "frontend",
        "lib",
    ],

    "backend": [
        "backend",
    ],
}


    def validate(
        self,
        project_path: Path,
    ) -> dict:

        errors = []

        for name, paths in self.REQUIRED.items():

            found = False

            for path in paths:

                if (
                    project_path / path
                ).exists():

                    found = True
                    break

            if not found:

                errors.append(
                    f"Missing {name}"
                )


        return {

            "success":
                len(errors) == 0,

            "project":
                str(project_path),

            "errors":
                errors,

        }
