from __future__ import annotations

from pathlib import Path
from string import Template

from ai.generators.base_generator import BaseGenerator


class FlutterGenerator(BaseGenerator):
    """
    Sino Builder AI
    Production Flutter Generator
    """

    def supports(self, file_path: str) -> bool:
        return Path(file_path).suffix.lower() == ".dart"

    def generate(
        self,
        file_path: str,
        description: str,
        prompt: str,
    ) -> str:

        text = prompt.lower()

        dark_theme = (
            "dark" in text
            or "داكن" in prompt
            or "ليلي" in prompt
        )

        glass = (
            "glass" in text
            or "زجاج" in prompt
        )

        background = (
            "0xff050816"
            if dark_theme
            else "0xffffffff"
        )

        panel = (
            "Colors.white10"
            if glass
            else "Colors.white"
        )

        template = Template(
            r'''
import 'package:flutter/material.dart';

void main() {
  runApp(const SinoGeneratedApp());
}

class SinoGeneratedApp extends StatelessWidget {
  const SinoGeneratedApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Sino Builder',
      theme: ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: const Color($background),
      ),
      home: const FutureHome(),
    );
  }
}

class FutureHome extends StatelessWidget {
  const FutureHome({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
            color: $panel,
            borderRadius: BorderRadius.circular(24),
          ),
          child: const Text(
            "Sino Builder AI",
            style: TextStyle(
              fontSize: 28,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
      ),
    );
  }
}
        '''
        )

        return template.substitute(
            background=background,
            panel=panel,
        )

