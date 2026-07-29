from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ProjectFile:
    path: str
    description: str



@dataclass
class FileManifest:

    files: list[ProjectFile] = field(
        default_factory=list
    )


    def add(
        self,
        path: str,
        description: str,
    ):

        self.files.append(
            ProjectFile(
                path,
                description
            )
        )



    def paths(self) -> list[str]:

        return [
            file.path
            for file in self.files
        ]
