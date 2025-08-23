import anthropic
from aegish.config import load_config


class ClaudeHandler:
    def __init__(self):
        config = load_config()
        self.model = config["model"]["api"]
        self.api_key = config.get('api_key')
        if not self.api_key:
            raise ValueError("No Claude API key found in config.")
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate(self, prompt: str) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content if hasattr(message, 'content') else str(message)