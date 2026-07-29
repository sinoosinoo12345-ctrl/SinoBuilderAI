from __future__ import annotations

from pathlib import Path

from dataclasses import dataclass


@dataclass
class UIScreen:
    name: str
    title: str


class FlutterUIGenerator:
    """
    Generates Flutter UI source files.
    """

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)

    def generate(self, screens: list[UIScreen]) -> None:

        screens_path = (
            self.project_path
            / "lib"
            / "screens"
        )

        screens_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        for screen in screens:

            filename = (
                screen.name.lower()
                + "_screen.dart"
            )

            file = screens_path / filename

            class_name = (
                screen.name.replace(" ", "")
                + "Screen"
            )

            content = f"""import 'package:flutter/material.dart';

class {class_name} extends StatelessWidget {{

  const {class_name}({{super.key}});

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(
        title: const Text('{screen.title}'),
      ),
      body: const Center(
        child: Text('{screen.name}'),
      ),
    );
  }}
}}
"""

            file.write_text(
                content,
                encoding="utf-8",
            )
