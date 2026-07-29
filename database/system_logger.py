from __future__ import annotations

from pathlib import Path
from datetime import datetime


class SystemLogger:
    """
    Global Sino Builder AI logger.
    """

    def __init__(
        self,
        file: str = "logs/system.log",
    ):

        self.file = Path(file)

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )


    def log(
        self,
        message: str,
    ):

        time = datetime.now().isoformat()

        line = (
            f"[{time}] {message}\n"
        )

        with self.file.open(
            "a",
            encoding="utf-8",
        ) as f:

            f.write(line)
