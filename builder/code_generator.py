from __future__ import annotations

from pathlib import Path
from typing import Union
from builder.templates.backend import BACKEND_TEMPLATE
from builder.templates.database import DATABASE_TEMPLATE
from builder.templates.frontend import FRONTEND_TEMPLATE
from builder.templates.flutter import FLUTTER_TEMPLATE


class CodeGenerator:
    """
    Sino Builder AI

    Universal Production Code Generator

    Responsible for generating every source file
    inside any generated project.
    """

    def __init__(self, project_path: Union[str, Path]):

        self.project_path = Path(project_path)

        self.generated_files = []

    # =======================================

    def write_file(
        self,
        relative_path: str,
        content: str,
    ) -> Path:

        file_path = self.project_path / relative_path

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path.write_text(
            content.strip() + "\n",
            encoding="utf-8",
        )

        self.generated_files.append(
            str(file_path)
        )

        return file_path

    # =======================================

    def create_folder(
        self,
        relative_path: str,
    ):

        (
            self.project_path / relative_path
        ).mkdir(
            parents=True,
            exist_ok=True,
        )

    # =======================================

    def create_tree(self):

        folders = [

            "backend",
            "backend/api",
            "backend/models",
            "backend/services",
            "backend/schemas",
            "backend/utils",

            "database",
            "database/migrations",

            "frontend",
            "frontend/assets",
            "frontend/assets/css",
            "frontend/assets/js",
            "frontend/assets/images",

            "docs",

            "tests",

        ]

        for folder in folders:

            self.create_folder(folder)
    # ==========================================
    # Backend Generator
    # ==========================================

    def create_backend(self):

        self.write_file(
            "backend/main.py",
            BACKEND_TEMPLATE["main"],
        )

        self.write_file(
            "backend/config/settings.py",
            BACKEND_TEMPLATE["settings"],
        )

        self.write_file(
            "backend/database.py",
            BACKEND_TEMPLATE["database"],
        )

        self.write_file(
            "backend/security.py",
            BACKEND_TEMPLATE["security"],
        )

        self.write_file(
            "backend/jwt.py",
            BACKEND_TEMPLATE["jwt"],
        )

        self.write_file(
            "backend/exceptions.py",
            BACKEND_TEMPLATE["exceptions"],
        )

        self.write_file(
            "backend/api/health.py",
            BACKEND_TEMPLATE["health"],
        )

        self.write_file(
            "backend/api/auth.py",
            BACKEND_TEMPLATE["auth_router"],
        )

        self.write_file(
            "backend/api/users.py",
            BACKEND_TEMPLATE["users_router"],
        )

        self.write_file(
            "backend/api/ai.py",
            BACKEND_TEMPLATE["ai_router"],
        )
    # ==========================================
    # Database Generator
    # ==========================================

    def create_database(self):

        self.write_file(
            "database/database.py",
            DATABASE_TEMPLATE["engine"],
        )

        self.write_file(
            "database/models.py",
            DATABASE_TEMPLATE["models"],
        )

        self.write_file(
            "database/crud.py",
            DATABASE_TEMPLATE["crud"],
        )

        self.write_file(
            "database/seed.py",
            DATABASE_TEMPLATE["seed"],
        )

        self.write_file(
            "database/schema.sql",
            DATABASE_TEMPLATE["migration"],
        )
   # ==========================================
    # Frontend Generator
    # ==========================================

    def create_frontend(self):

        self.write_file(
            "frontend/index.html",
            FRONTEND_TEMPLATE["index"],
        )

        self.write_file(
            "frontend/assets/css/style.css",
            FRONTEND_TEMPLATE["style"],
        )

        self.write_file(
            "frontend/assets/js/app.js",
            FRONTEND_TEMPLATE["javascript"],
        )

        self.write_file(
            "frontend/home.html",
            FRONTEND_TEMPLATE["home"],
        )

        self.write_file(
            "frontend/dashboard.html",
            FRONTEND_TEMPLATE["dashboard"],
        )

        self.write_file(
            "frontend/settings.html",
            FRONTEND_TEMPLATE["settings"],
        )

    def create_flutter(self):

        self.write_file(
            "flutter/pubspec.yaml",
            FLUTTER_TEMPLATE["pubspec"],
        )

        self.write_file(
            "flutter/lib/main.dart",
            FLUTTER_TEMPLATE["main"],
        )

        self.write_file(
            "flutter/lib/core/router/app_router.dart",
            FLUTTER_TEMPLATE["router"],
        )

        self.write_file(
            "flutter/lib/core/theme/app_theme.dart",
            FLUTTER_TEMPLATE["theme"],
        )

        self.write_file(
            "flutter/lib/core/providers/app_provider.dart",
            FLUTTER_TEMPLATE["provider"],
        )

        self.write_file(
            "flutter/lib/core/network/api.dart",
            FLUTTER_TEMPLATE["network"],
        )

        self.write_file(
            "flutter/lib/core/storage/storage.dart",
            FLUTTER_TEMPLATE["storage"],
        )

        self.write_file(
            "flutter/lib/core/services/api_service.dart",
            FLUTTER_TEMPLATE["service"],
        )

        self.write_file(
            "flutter/lib/features/home/home_screen.dart",
            FLUTTER_TEMPLATE["home"],
        )

        self.write_file(
            "flutter/lib/features/dashboard/dashboard_screen.dart",
            FLUTTER_TEMPLATE["dashboard"],
        )

        self.write_file(
            "flutter/lib/features/settings/settings_screen.dart",
            FLUTTER_TEMPLATE["settings"],
        )
    # ==========================================
    # API Generator
    # ==========================================

    def create_api(self):

        self.write_file(
            "backend/api/auth.py",
            """
from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {
        "token":"demo"
    }

@router.post("/register")
def register():
    return {
        "status":"created"
    }
""",
        )

        self.write_file(
            "backend/api/users.py",
            """
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def users():
    return []
""",
        )

        self.write_file(
            "backend/api/ai.py",
            """
from fastapi import APIRouter

router = APIRouter()

@router.get("/analyze")
def analyze():
    return {
        "status":"ready"
    }
""",
        )

    # ==========================================
    # Project Generator
    # ==========================================

    def create_project(self):

        self.create_tree()

        self.create_backend()

        self.create_database()

        self.create_frontend()

        self.create_flutter()
    # ==========================================
    # Summary
    # ==========================================

    def summary(self):

        return {
            "success": True,
            "project": str(self.project_path),
            "generated_files": self.generated_files,
            "count": len(self.generated_files),
        }
