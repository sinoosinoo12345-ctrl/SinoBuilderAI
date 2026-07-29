from __future__ import annotations

from builder.project_manager import ProjectManager


def main():

    print("=" * 50)
    print("   Sino Builder AI - Projects")
    print("=" * 50)

    manager = ProjectManager()

    projects = manager.list_projects()

    if not projects:

        print("No projects found.")

        return


    for index, project in enumerate(
        projects,
        start=1,
    ):

        print()

        print(
            f"{index}. {project['name']}"
        )

        print(
            "Path:",
            project["path"]
        )

        if "description" in project:

            print(
                "Description:",
                project["description"]
            )

            print(
                "Changes:",
                project["changes"]
            )


if __name__ == "__main__":

    main()
