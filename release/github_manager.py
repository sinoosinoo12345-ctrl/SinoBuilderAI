from __future__ import annotations

import subprocess
from pathlib import Path


class GitHubManager:

    def __init__(self, repo_root: str, github_user: str):
        self.repo = Path(repo_root)
        self.github_user = github_user

    def create_repository(self, project_name: str):

        subprocess.run(
            [
                "gh",
                "repo",
                "create",
                project_name,
                "--public",
                "--source",
                str(self.repo),
                "--remote",
                "origin",
                "--push",
            ],
            cwd=self.repo,
            check=True,
        )

    def commit(self, message: str):

        subprocess.run(
            ["git", "add", "."],
            cwd=self.repo,
            check=True,
        )

        subprocess.run(
            [
                "git",
                "commit",
                "-m",
                message,
            ],
            cwd=self.repo,
            check=False,
        )

    def push(self):

        subprocess.run(
            [
                "git",
                "push",
                "origin",
                "main",
            ],
            cwd=self.repo,
            check=True,
        )

    def publish(self, project_name: str):

        if not (self.repo / ".git").exists():

            subprocess.run(
                ["git", "init"],
                cwd=self.repo,
                check=True,
            )

            subprocess.run(
                [
                    "git",
                    "branch",
                    "-M",
                    "main",
                ],
                cwd=self.repo,
                check=False,
            )

            self.create_repository(project_name)

        self.commit(f"Initial Release: {project_name}")

        self.push()

        return {
            "status": "published",
            "repository": f"https://github.com/{self.github_user}/{project_name}",
        }
