import re

class PostProcessor:
    @staticmethod
    def clean(command: str) -> str:
        # Remove triple backticks and language tags
        command = re.sub(r'^```[a-zA-Z]*\s*', '', command.strip())
        command = re.sub(r'```$', '', command.strip())
        command = command.strip('`').strip()
        command = re.sub(r'^(shell|bash|sh|zsh)\s*', '', command, flags=re.IGNORECASE)
        return command
