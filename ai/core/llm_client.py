import requests

from ai.core.provider_manager import ProviderManager


class LLMClient:

    def __init__(self):

        self.providers = ProviderManager()

    def ask(self, prompt):

        provider = self.providers.active()

        if provider is None:

            return {
                "success": False,
                "error": "No AI Provider Enabled"
            }

        if provider.name == "Local AI":

            return {
                "success": True,
                "provider": "Local AI",
                "message": "Local AI connector ready"
            }

        if provider.name == "OpenAI":

            return {
                "success": True,
                "provider": "OpenAI",
                "message": "OpenAI connector ready"
            }

        return {
            "success": False,
            "error": "Unknown Provider"
        }
