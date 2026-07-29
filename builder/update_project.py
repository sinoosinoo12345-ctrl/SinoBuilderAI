from __future__ import annotations

from pathlib import Path

from builder.update_engine import UpdateEngine


def main():

    print("=" * 50)
    print("   Sino Builder AI - Update")
    print("=" * 50)

    project_name = input(
        "Project name: "
    ).strip()

    request = input(
        "What should be changed: "
    ).strip()

    project_path = (
        Path("workspace")
        / project_name
    )

    engine = UpdateEngine(
        str(project_path)
    )

    result = engine.update(
        request
    )

    print("\nUpdate Saved:")
    print(result)


if __name__ == "__main__":
    main()
