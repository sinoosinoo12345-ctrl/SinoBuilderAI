from ai.core.llm_client import LLMClient
from ai.core.project_analyzer import ProjectAnalyzer
from ai.core.project_spec import UniversalProjectSpec


class SinoBrain:

    def __init__(self):

        self.llm = LLMClient()
        self.analyzer = ProjectAnalyzer()

    def think(self, description):

        analysis = self.analyzer.analyze(description)

        spec = UniversalProjectSpec(
            name=analysis.name,
            description=analysis.description,
            goal=description,
            frontend=analysis.pages,
            backend=analysis.services,
            database=analysis.entities,
            api=[],
            ai_modules=["Sino AI"] if analysis.ai_required else []
        )

        llm_result = self.llm.ask(description)

        return {
            "spec": spec,
            "llm": llm_result,
            "status": "Brain Ready"
        }
