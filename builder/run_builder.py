from __future__ import annotations

from pathlib import Path

from builder.project_pipeline import ProjectPipeline



def main():

    print("=" * 50)
    print("       Sino Builder AI")
    print("=" * 50)


    name = input(
        "Project name: "
    ).strip()


    idea = input(
        "Application idea: "
    ).strip()


    if not name:
        raise ValueError(
            "Project name is required"
        )


    if not idea:
        raise ValueError(
            "Application idea is required"
        )


    project_path = (
        Path("workspace")
        / name
    )


    project_path.mkdir(
        parents=True,
        exist_ok=True,
    )


    pipeline = ProjectPipeline()


    result = pipeline.build(
        str(project_path),
        name,
        idea,
    )


    print("\n" + "=" * 50)
    print("BUILD RESULT")
    print("=" * 50)

   for key, value in result.items():
        print(f"{key}: {value}")
    )

if __name__ == "__main__":

    main()
