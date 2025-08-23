import re

class PostProcessor:
    @staticmethod
    def clean(command: str) -> str:
        # Remove triple backticks and language tags
        # Even though the system prompt says only the command,
        # LLMs still add tags so this strips those and just returns the raw command
        command = re.sub(r'^```[a-zA-Z]*\s*', '', command.strip())
        command = re.sub(r'```$', '', command.strip())
        command = command.strip('`').strip()
        command = re.sub(r'^(shell|bash|sh|zsh)\s*', '', command, flags=re.IGNORECASE)
        return command
