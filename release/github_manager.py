from __future__ import annotations

import subprocess
from pathlib import Path


class GitHubManager:

    def __init__(self, repo_root: str):
        self.repo = Path(repo_root)

    def commit(self, message: str):

        subprocess.run(["git", "add", "."], cwd=self.repo, check=True)

        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=self.repo,
            check=False,
        )

    def push(self):

        subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=self.repo,
            check=True,
        )

    def publish(self, message: str):

        self.commit(message)

        self.push()

        return {
            "status": "published",
            "repository": str(self.repo),
        }
