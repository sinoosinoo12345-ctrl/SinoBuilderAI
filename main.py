from builder.project_pipeline import ProjectPipeline


def main():

    print("=" * 50)
    print("        Sino Builder AI")
    print("=" * 50)


    project_name = input("Project Name: ").strip()

    prompt = input(
        "Describe your application: "
    ).strip()


    pipeline = ProjectPipeline()


    result = pipeline.build(
        project_path=f"workspace/{project_name}",
        project_name=project_name,
        requirements=prompt,
    )


    print("\nProject Created Successfully")

    print(
        f"Name : {project_name}"
    )

    print(
        f"Path : workspace/{project_name}"
    )


    print("\nPipeline Status:")

    for key in result.keys():

        print(
            f"✓ {key}"
        )


if __name__ == "__main__":
    main()
