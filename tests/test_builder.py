from __future__ import annotations

import shutil
from pathlib import Path

from builder.project_pipeline import ProjectPipeline



TEST_PROJECT = "TestAutoBuild"



def test_project_generation():

    project_path = (
        Path("workspace")
        / TEST_PROJECT
    )


    if project_path.exists():

        shutil.rmtree(
            project_path
        )


    pipeline = ProjectPipeline()


    result = pipeline.build(
        str(project_path),
        TEST_PROJECT,
        "تطبيق إدارة مطعم مع طلبات وفواتير"
    )


    assert result

    generated_files = [
        item["file"]
        for item in result
    ]


    assert len(
        generated_files
    ) > 0


    for file in generated_files:

        assert Path(
            file
        ).exists()



def test_python_files_created():

    project_path = (
        Path("workspace")
        / TEST_PROJECT
    )


    python_files = list(
        project_path.rglob("*.py")
    )


    assert len(
        python_files
    ) > 0
