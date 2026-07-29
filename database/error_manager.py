from __future__ import annotations

from pathlib import Path
from datetime import datetime


class ErrorManager:
    """
    Handles system errors and recovery logs.
    """

    def __init__(
        self,
        file: str = "logs/errors.log",
    ):

        self.file = Path(file)

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )


    def record(
        self,
        error: str,
    ):

        timestamp = datetime.now().isoformat()

        message = (
            f"[{timestamp}] ERROR: {error}\n"
        )

        with self.file.open(
            "a",
            encoding="utf-8",
        ) as f:

            f.write(message)


    def last_errors(
        self,
        limit: int = 10,
    ):

        if not self.file.exists():

            return []

        lines = self.file.read_text(
            encoding="utf-8"
        ).splitlines()

        return lines[-limit:]
