from __future__ import annotations

import platform
import shutil
import subprocess


def check_python():
    return {
        "name": "Python",
        "ok": True,
        "version": platform.python_version(),
    }


def check_command(command, title, fix):
    path = shutil.which(command)

    if path is None:
        return {
            "name": title,
            "ok": False,
            "reason": f"{title} is not installed.",
            "fix": fix,
        }

    try:
        result = subprocess.run(
            [command, "--version"],
            capture_output=True,
            text=True,
            timeout=10,
        )

        version = (result.stdout or result.stderr).strip()

        return {
            "name": title,
            "ok": True,
            "version": version,
        }

    except Exception as e:
        return {
            "name": title,
            "ok": False,
            "reason": str(e),
            "fix": fix,
        }


def run_all_checks():
    return [
        check_python(),
        check_command(
            "git",
            "Git",
            "pkg install git",
        ),
        check_command(
            "java",
            "Java",
            "pkg install openjdk-21",
        ),
        check_command(
            "gradle",
            "Gradle",
            "Use Gradle Wrapper or install Gradle.",
        ),
        check_command(
            "flutter",
            "Flutter",
            "Install Flutter compatible with Termux.",
        ),
        check_command(
            "dart",
            "Dart",
            "Repair Flutter/Dart SDK.",
        ),
    ]
