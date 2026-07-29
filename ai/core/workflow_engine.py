from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class WorkflowStep:

    name: str

    enabled: bool = True

    required: bool = True

    retries: int = 1

    timeout: int = 300



class WorkflowEngine:
    """
    Sino Builder AI

    Production Application Creation Workflow.
    """


    def __init__(self):

        self.steps: list[WorkflowStep] = [

            WorkflowStep(
                "Requirement"
            ),

            WorkflowStep(
                "Planner"
            ),

            WorkflowStep(
                "Architecture"
            ),

            WorkflowStep(
                "UI Design"
            ),

            WorkflowStep(
                "Backend"
            ),

            WorkflowStep(
                "Database"
            ),

            WorkflowStep(
                "AI"
            ),

            WorkflowStep(
                "Code Generation"
            ),

            WorkflowStep(
                "Testing"
            ),

            WorkflowStep(
                "Cyber Security"
            ),

            WorkflowStep(
                "Optimization"
            ),

            WorkflowStep(
                "Documentation"
            ),

            WorkflowStep(
                "Integration"
            ),

            WorkflowStep(
                "Release"
            ),

            WorkflowStep(
                "Memory"
            ),

        ]



    def get_steps(
        self,
    ) -> list[WorkflowStep]:

        return [
            step
            for step in self.steps
            if step.enabled
        ]



    def enable(
        self,
        name: str,
    ):

        for step in self.steps:

            if step.name == name:

                step.enabled = True

                return



    def disable(
        self,
        name: str,
    ):

        for step in self.steps:

            if step.name == name:

                step.enabled = False

                return
