from builder.code_generator import CodeGenerator
from release.release_pipeline import ReleasePipeline


class ReleaseAgent:

    def run(self, project_path, task):

        generator = CodeGenerator(project_path)

        pipeline = ReleasePipeline()

        release = pipeline.create_release(
            project_path,
            task.get("project_name", "SinoProject"),
        )

        return {
            "status": "Cloud Release Ready",
            "generated": generator.summary(),
            "release": release,
        }
