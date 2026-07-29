from dataclasses import dataclass


@dataclass
class Provider:

    name: str

    enabled: bool

    api_key: str = ""

    endpoint: str = ""


class ProviderManager:

    def __init__(self):

        self.providers = {

            "openai": Provider(
                name="OpenAI",
                enabled=False,
                endpoint="https://api.openai.com/v1"
            ),

            "local": Provider(
                name="Local AI",
                enabled=True,
                endpoint="http://127.0.0.1:11434"
            ),

            "custom": Provider(
                name="Custom",
                enabled=False,
                endpoint=""
            )

        }

    def list(self):

        return {
            k: vars(v)
            for k, v in self.providers.items()
        }

    def enable(self, provider):

        if provider in self.providers:

            self.providers[provider].enabled = True

    def disable(self, provider):

        if provider in self.providers:

            self.providers[provider].enabled = False

    def set_key(self, provider, key):

        if provider in self.providers:

            self.providers[provider].api_key = key

    def active(self):

        for p in self.providers.values():

            if p.enabled:

                return p

        return None
