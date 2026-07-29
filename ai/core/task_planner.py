from ai.core.project_spec import UniversalProjectSpec


class TaskPlanner:

    def build(self, spec: UniversalProjectSpec):

        tasks = []

        for page in spec.frontend:
            tasks.append({
                "agent": "UIDesigner",
                "type": "frontend",
                "target": page
            })

        for service in spec.backend:
            tasks.append({
                "agent": "Backend",
                "type": "backend",
                "target": service
            })

        for table in spec.database:
            tasks.append({
                "agent": "Database",
                "type": "database",
                "target": table
            })

        for api in spec.api:
            tasks.append({
                "agent": "Backend",
                "type": "api",
                "target": api
            })

        for module in spec.ai_modules:
            tasks.append({
                "agent": "AI",
                "type": "ai",
                "target": module
            })

        tasks.append({
            "agent": "Cyber",
            "type": "security",
            "target": "Full Scan"
        })

        tasks.append({
            "agent": "Release",
            "type": "release",
            "target": "Build Package"
        })

        return tasks
