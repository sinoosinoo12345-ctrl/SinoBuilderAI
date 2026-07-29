from pathlib import Path


class DatabaseEngineer:

    def run(self, project_path):

        project = Path(project_path)

        database = project / "database"

        (database / "database.py").write_text(
'''from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///app.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
''',
            encoding="utf-8"
        )

        (database / "models" / "base.py").write_text(
'''from sqlalchemy.orm import declarative_base

Base = declarative_base()
''',
            encoding="utf-8"
        )

        return {
            "status": "Database Generated"
        }
