from builder.code_generator import CodeGenerator


class ReleaseAgent:

    def run(self, project_path, task):

        generator = CodeGenerator(project_path)

        return {
            "status": "Release Ready",
            "generated": generator.summary(),
        }
