from __future__ import annotations

from pathlib import Path


class TemplateLoader:
    """
    Sino Builder AI
    Template Loader
    Release V1
    """

    def __init__(
        self,
        template_root: str = "templates",
    ):

        self.template_root = Path(
            template_root
        )

    def exists(
        self,
        template_name: str,
    ) -> bool:

        return (
            self.template_root
            / template_name
        ).exists()

    def path(
        self,
        template_name: str,
    ) -> Path:

        return (
            self.template_root
            / template_name
        )

    def list_files(
        self,
        template_name: str,
    ) -> list[Path]:

        folder = self.path(
            template_name
        )

        if not folder.exists():
            return []

        return [

            file

            for file in folder.rglob("*")

            if file.is_file()

        ]

    def list_templates(
        self,
    ) -> list[str]:

        if not self.template_root.exists():
            return []

        return sorted(
            folder.name
            for folder in self.template_root.iterdir()
            if folder.is_dir()
        )
