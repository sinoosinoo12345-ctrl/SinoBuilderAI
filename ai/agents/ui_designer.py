from builder.code_generator import CodeGenerator


class UIDesigner:

    def generate(self, spec):

        screens = []

        for screen in getattr(spec, "screens", []):
            screens.append(screen)

        return screens


    def run(self, project_path, task):

        generator = CodeGenerator(project_path)

        generator.create_frontend()

        return {
            "status": "UI Generated",
            "generated": generator.generated_files,
        }
