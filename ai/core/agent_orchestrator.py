from __future__ import annotations

from ai.core.agent_context import AgentContext
from ai.core.agent_factory import AgentFactory
from ai.core.agent_registry import register_all
from ai.core.workflow_engine import WorkflowEngine
from ai.core.agent_memory_bus import AgentMemoryBus


class AgentOrchestrator:
    """
    Sino Builder AI
    Production Agent Orchestrator.

    Coordinates application development agents.
    Cyber Security is handled by Security Agent.
    """

    def __init__(self):

        register_all()

        self.workflow = WorkflowEngine()

        self.memory = AgentMemoryBus()



    def execute(
        self,
        context: AgentContext,
    ) -> AgentContext:


        context.metadata["workflow"] = []


        for step in self.workflow.get_steps():

            try:

                agent = AgentFactory.create(
                    step.name
                )


                context.metadata["memory_bus"] = (
                    self.memory.snapshot()
                )


                context = agent.run(
                    context
                )


                execution = {

                    "agent": step.name,

                    "status": "success",

                }


                context.metadata["workflow"].append(
                    execution
                )


                self.memory.add_decision(
                    f"{step.name}: completed"
                )


                result = context.metadata.get(
                    step.name
                )


                if result:

                    self.memory.add_architecture_note(
                        str(result)
                    )


            except Exception as error:


                message = (
                    f"{step.name} failed: {error}"
                )


                context.add_error(
                    message
                )


                context.metadata["workflow"].append({

                    "agent": step.name,

                    "status": "failed",

                    "error": str(error),

                })


                self.memory.add_warning(
                    message
                )


                if getattr(
                    step,
                    "required",
                    True
                ):

                    break



        context.metadata["memory_bus"] = (
            self.memory.snapshot()
        )


        return context
