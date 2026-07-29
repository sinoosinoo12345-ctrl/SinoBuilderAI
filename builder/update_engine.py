from __future__ import annotations

from pathlib import Path

from database.project_memory import ProjectMemory
from database.version_manager import VersionManager
from database.system_logger import SystemLogger
from database.error_manager import ErrorManager

from builder.change_analyzer import ChangeAnalyzer

from ai.core.code_generation_engine import CodeGenerationEngine
from ai.core.agent_context import AgentContext


class UpdateEngine:
    """
    Updates projects safely with:
    - Backup
    - Memory
    - Logging
    - Error recovery
    - Agent Context
    """

    def __init__(
        self,
        project_path: str,
    ):

        self.project_path = Path(
            project_path
        )

        self.memory = ProjectMemory(
            project_path
        )

        self.version = VersionManager(
            project_path
        )

        self.analyzer = ChangeAnalyzer()

        self.generator = CodeGenerationEngine()

        self.logger = SystemLogger()

        self.errors = ErrorManager()


    def update(
        self,
        request: str,
    ):

        try:

            project = self.memory.load()

            if project is None:
                raise FileNotFoundError(
                    "Project memory not found"
                )


            backup = self.version.create_backup()


            self.logger.log(
                f"Backup created: {backup}"
            )


            context = AgentContext(
                request=request,
                project=self.project_path.name,
            )


            affected_files = self.analyzer.analyze(
                request
            )


            updated = []


            for file in affected_files:

                path = self.generator.generate_and_save(

                    str(self.project_path),

                    file,

                    f"Update file according to: {request}",

                    context

                )


                updated.append(
                    path
                )

                context.add_generated_file(
                    path
                )


            self.memory.add_change(
                f"Updated files for: {request}"
            )


            self.logger.log(
                f"Project updated: {request}"
            )


            return {

                "success": True,

                "backup": backup,

                "updated_files": updated,

            }


        except Exception as e:


            self.errors.record(
                str(e)
            )


            self.logger.log(
                f"Update failed: {e}"
            )


            return {

                "success": False,

                "error": str(e),

            }
