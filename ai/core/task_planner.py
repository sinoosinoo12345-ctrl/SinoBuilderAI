from ai.core.project_spec import UniversalProjectSpec


class TaskPlanner:

    def build(self, spec: UniversalProjectSpec):

        return [

            {
                "agent": "AI",
                "type": "project",
                "target": "Full Project"
            },

            {
                "agent": "Cyber",
                "type": "security",
                "target": "Full Scan"
            },

            {
                "agent": "Release",
                "type": "release",
                "target": "Flutter Build"
            },

        ]
