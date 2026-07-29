from __future__ import annotations

from pathlib import Path


class DatabaseGenerator:
    """
    Generates the database structure.
    """

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)

    def generate(self) -> None:

        database = self.project_path / "database"

        database.mkdir(
            parents=True,
            exist_ok=True,
        )

        (database / "__init__.py").write_text(
            "",
            encoding="utf-8",
        )

        (database / "models.py").write_text(
            '''
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
'''.strip(),
            encoding="utf-8",
        )

        (database / "session.py").write_text(
            '''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database/app.db"

engine = create_engine(
    DATABASE_URL,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
'''.strip(),
            encoding="utf-8",
        )
