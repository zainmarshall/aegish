
from google import genai
from aegish.config import load_config
from aegish.debug import print_debug


class GeminiHandler:
    def __init__(self):
        config = load_config()
        api_key = config.get('api_key')
        model = config.get('model').get('api')
        if not api_key:
            raise ValueError("No Gemini API key found in config.")
        self.model = model
        self.client = genai.Client(api_key=api_key)
        print_debug(f"GeminiHandler model: {self.model}")
        print_debug(f"GeminiHandler client: {self.client}")

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model, contents=prompt
        )
        print_debug(f"Gemini API raw response: {response}")
        return response.text

