from __future__ import annotations

from pathlib import Path


class SinoCyberAI:

    def __init__(self):

        self.name = "Sino Cyber AI"

    def scan_project(self, project_path):

        project = Path(project_path)

        issues = []

        checks = [
            ".env",
            "requirements.txt",
            "release.json",
        ]

        for item in checks:

            if not (project / item).exists():

                issues.append(f"Missing: {item}")

        return {
            "engine": self.name,
            "secure": len(issues) == 0,
            "issues": issues,
            "score": max(0, 100 - len(issues) * 20),
        }

    def review_code(self, text: str):

        warnings = []

        if "eval(" in text:

            warnings.append("Dangerous eval() detected")

        if "exec(" in text:

            warnings.append("Dangerous exec() detected")

        if "password=" in text.lower():

            warnings.append("Hardcoded password detected")

        return {
            "warnings": warnings,
            "safe": len(warnings) == 0,
        }
    def run(self, project_path, task):

        return self.scan_project(project_path)
