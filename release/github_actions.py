from __future__ import annotations

import subprocess
import time


class GitHubActions:

    def wait(self, seconds: int = 30):

        time.sleep(seconds)

        return {
            "status": "waiting_complete"
        }

    def last_run(self):

        try:

            result = subprocess.run(
                [
                    "gh",
                    "run",
                    "list",
                    "--limit",
                    "1",
                ],
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "success": True,
                "output": result.stdout,
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e),
            }
