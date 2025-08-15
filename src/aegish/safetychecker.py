from typing import Tuple

class SafetyChecker:
    BLACKLIST = {
        "rm -rf /",
        "rm -rf --no-preserve-root /",
        "mkfs",
        "dd if=",
        ":(){ :|:& };:",
    }
    MAX_PROMPT_LENGTH = 2000  

    @classmethod
    def check(cls, text: str) -> Tuple[bool, str]:
        lower = text.lower()
        for bad in cls.BLACKLIST:
            if bad in lower:
                return False, f"Output contains blocked token: {bad}"
        return True, ""
