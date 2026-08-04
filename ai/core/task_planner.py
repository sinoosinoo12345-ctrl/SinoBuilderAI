from ai.core.project_spec import UniversalProjectSpec


class TaskPlanner:

    def build(self, spec: UniversalProjectSpec):

        return [

            {
                "agent": "Planner",
                "type": "planning",
                "target": "Project Planning",
            },

            {
                "agent": "Architect",
                "type": "architecture",
                "target": "System Architecture",
            },

            {
                "agent": "UIDesigner",
                "type": "ui",
                "target": "Modern UI/UX",
            },

            {
                "agent": "Backend",
                "type": "backend",
                "target": "Backend API",
            },

            {
                "agent": "Database",
                "type": "database",
                "target": "Database",
            },

            {
                "agent": "AI",
                "type": "project",
                "target": "Full Project",
            },

            {
                "agent": "Cyber",
                "type": "security",
                "target": "Security Scan",
            },

            {
                "agent": "Release",
                "type": "release",
                "target": "Flutter Release",
            },

        ]
