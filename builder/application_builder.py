from __future__ import annotations

from ai.core.spec_generator import SpecificationGenerator
from ai.agents.ui_designer import UIDesigner

from builder.backend_generator import BackendGenerator
from builder.database_generator import DatabaseGenerator
from builder.flutter_ui_generator import FlutterUIGenerator


class ApplicationBuilder:
    """
    Coordinates generation of a complete application.
    """

    def __init__(self, project_path: str):
        self.project_path = project_path

    def build(self, prompt: str):

        spec = SpecificationGenerator().generate(prompt)

        ui = UIDesigner().generate(spec)

        FlutterUIGenerator(
            self.project_path
        ).generate(ui)

        BackendGenerator(
            self.project_path
        ).generate()

        DatabaseGenerator(
            self.project_path
        ).generate()

        return spec
