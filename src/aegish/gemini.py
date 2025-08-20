
from google import genai
from aegish.config import load_config

class GeminiHandler:
    def __init__(self):
        config = load_config()
        api_key = config.get('api_key')
        model = config.get('model', 'gemini-2.5-flash')
        if not api_key:
            raise ValueError("No Gemini API key found in config.")
        self.model = model
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model, contents=prompt
        )
        return response.text

