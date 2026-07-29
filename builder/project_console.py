from __future__ import annotations

from builder.project_manager import ProjectManager
from builder.update_engine import UpdateEngine
from builder.project_status import ProjectStatus


def main():

    print("=" * 50)
    print("   Sino Builder AI - Console")
    print("=" * 50)

    manager = ProjectManager()
    status = ProjectStatus()

    projects = manager.list_projects()

    if not projects:

        print("No projects found.")
        return


    print("\nProjects:\n")

    for index, project in enumerate(
        projects,
        start=1,
    ):

        print(
            f"{index}. {project['name']}"
        )


    choice = input(
        "\nSelect project number: "
    ).strip()


    if not choice.isdigit():

        print("Invalid selection")
        return


    number = int(choice)

    if number < 1 or number > len(projects):

        print("Project not found")
        return


    selected = projects[number - 1]


    print(
        "\nSelected:",
        selected["name"]
    )


    info = status.analyze(
        selected["path"]
    )


    print("\nProject Status:")

    print(
        "Files:",
        info["files"]
    )

    print(
        "Changes:",
        info["changes"]
    )

    print(
        "Backups:",
        info["backups"]
    )


    request = input(
        "\nWhat should be changed: "
    ).strip()


    if request:

        engine = UpdateEngine(
            selected["path"]
        )

        result = engine.update(
            request
        )

        print("\nUpdate Result:")
        print(result)


if __name__ == "__main__":

    main()
