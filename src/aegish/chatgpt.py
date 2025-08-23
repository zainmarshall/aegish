
from openai import OpenAI
from aegish.config import load_config


class OpenAIHandler:
    def __init__(self):
        config = load_config()
        self.model = config["model"]["api"]
        self.api_key = config.get('api_key')
        if not self.api_key:
            raise ValueError("No OpenAI API key found in config.")
        self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )
        # OpenAI API returns choices[0].message.content
        return response.choices[0].message.content.strip()