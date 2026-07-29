from __future__ import annotations

from ai.core.agent_context import AgentContext
from ai.core.agent_orchestrator import AgentOrchestrator
from ai.core.architecture_engine import ArchitectureEngine
from ai.core.manifest_builder import ManifestBuilder


class SinoAssistant:
    """
    Sino Builder AI Executive.

    Coordinates application development agents.
    Security tasks are handled by Cyber Security Agent.
    """

    def __init__(self):

        self.orchestrator = AgentOrchestrator()

        self.architecture = ArchitectureEngine()

        self.manifest = ManifestBuilder()



    def execute(
        self,
        project_name: str,
        request: str,
    ):


        context = AgentContext(

            request=request,

            project=project_name,

        )


        context = self.orchestrator.execute(
            context
        )


        architecture = self.architecture.analyze(

            project_name,

            request,

        )


        context.architecture = (
            architecture.summary()
        )


        manifest = self.manifest.build(
            architecture
        )


        return {

            "context": context,

            "architecture": architecture,

            "manifest": manifest,

        }
