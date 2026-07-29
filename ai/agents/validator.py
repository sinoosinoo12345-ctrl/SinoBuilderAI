from __future__ import annotations

import ast
from pathlib import Path


class ValidatorAgent:
    """
    Sino Builder AI

    Production Quality Validator.

    Checks generated applications
    before build and release.
    """


    def validate_python(
        self,
        file_path: str,
    ) -> dict:

        path = Path(file_path)

        if not path.exists():
            return {
                "success": False,
                "file": str(path),
                "error": "File does not exist",
            }

        try:

            source = path.read_text(
                encoding="utf-8"
            )

            ast.parse(source)

            return {
                "success": True,
                "file": str(path),
                "message": (
                    "Python syntax valid"
                ),
            }


        except SyntaxError as error:

            return {
                "success": False,
                "file": str(path),
                "error": str(error),
            }


    def validate_structure(
        self,
        project_path: str,
    ) -> dict:

        path = Path(project_path)

        required = [
            "README.md",
            "config",
            "backend",
            "frontend",
        ]

        missing = []

        for item in required:

            if not (path / item).exists():
                missing.append(item)


        return {
            "success": len(missing) == 0,
            "missing": missing,
            "message": (
                "Project structure valid"
                if not missing
                else "Missing project components"
            ),
        }


    def validate(
        self,
        file_path: str,
    ) -> dict:

        path = Path(file_path)

        if path.suffix == ".py":

            return self.validate_python(
                file_path
            )


        return {
            "success": True,
            "file": file_path,
            "message": (
                "No validator required"
            ),
        }


    def full_check(
        self,
        project_path: str,
    ) -> dict:

        structure = self.validate_structure(
            project_path
        )

        return {
            "project": project_path,
            "structure": structure,
            "ready": structure["success"],
        }
