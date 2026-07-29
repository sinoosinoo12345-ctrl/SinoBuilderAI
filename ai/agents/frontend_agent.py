from __future__ import annotations

from ai.agents.base_agent import BaseAgent
from ai.agents.agent_profile import AgentProfile


class FrontendAgent(BaseAgent):

    PROFILE = AgentProfile(
        name="Frontend",
        role="Senior Futuristic UI Engineer",

        expertise=(
            "Flutter, Web UI, Glassmorphism, "
            "3D Interfaces, Responsive Design"
        ),

        system_prompt="""
You are Sino Builder AI Frontend Architect.

Your mission:
Create futuristic application interfaces.

Design principles:
- Modern 2035 visual style.
- Glassmorphism.
- 3D depth layers.
- Smooth animations.
- Responsive layouts.
- Premium user experience.

For every application define:

1. Screen structure.
2. Navigation system.
3. UI components.
4. 3D visual elements.
5. Animations.
6. User interactions.

Never create basic old-style interfaces.
Always design premium modern experiences.
"""
    )


    def design_interface(
        self,
        project_name: str,
        features: list[str],
    ) -> dict:

        return {
            "project": project_name,

            "design_system": {
                "style": "Futuristic 2035 Glass 3D",
                "depth": True,
                "lighting": "Cinematic",
                "animations": True,
                "responsive": True,
            },

            "screens": [
                {
                    "name": "Home",
                    "type": "3D Dashboard",
                    "components": [
                        "Glass Panels",
                        "Animated Navigation",
                        "AI Assistant",
                        "Interactive Cards",
                    ],
                },

                {
                    "name": "Profile",
                    "type": "Holographic Profile",
                    "components": [
                        "3D Avatar",
                        "Statistics",
                        "Settings",
                    ],
                },
            ],

            "features": features,

            "ready_for_generation": True,
        }
