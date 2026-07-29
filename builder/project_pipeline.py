from __future__ import annotations

from pathlib import Path

from builder.application_builder import ApplicationBuilder
from builder.flutter_project_builder import FlutterProjectBuilder
from release.release_pipeline import ReleasePipeline


class ProjectPipeline:

    def __init__(self):

        self.application = ApplicationBuilder

        self.flutter = FlutterProjectBuilder()

        self.release = ReleasePipeline()

    def build(
        self,
        project_path: str,
        project_name: str,
        requirements: str,
    ):
        project = Path(project_path)
        project.mkdir(parents=True, exist_ok=True)

        builder = self.application(str(project))
        specification = builder.build(requirements)

        flutter_project = project / project_name.lower().replace(" ", "_")

        apk = None
        flutter_status = "disabled"

        try:
            self.flutter.create(str(flutter_project))
            self.flutter.pub_get(str(flutter_project))
            apk = self.flutter.build_release(str(flutter_project))
            flutter_status = "success"
        except Exception as e:
            print(f"\n⚠ Flutter build skipped: {e}")
            flutter_status = "failed"

        release = self.release.create_release(
            project_path=str(project),
            project_name=project_name,
        )

        if apk:
            release["apk"] = str(apk)

        return {
            "status": "success",
            "project": project_name,
            "path": str(project),
            "specification": specification,
            "flutter": flutter_status,
            "apk": str(apk) if apk else None,
            "release": release,
        }
