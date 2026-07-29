from builder.code_generator import CodeGenerator


class ProgrammerAgent:

    def __init__(self):
        pass

    def run(self, project_path, task):

        generator = CodeGenerator(project_path)

        generator.create_project()

        return {
            "success": True,
            "status": "Project Generated"
        }

    def build(self, project_path, architecture=None, target=None):

        return self.run(
            project_path,
            {
                "target": target
            }
        )
