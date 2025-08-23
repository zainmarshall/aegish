
import subprocess
import shutil

# it handles ollama... genius naming right?

class OllamaHandler:
    def __init__(self):
        from aegish.config import load_config
        config = load_config()
        self.model = config["model"]["api"]
        self.exe = shutil.which("ollama")
        if not self.exe:
            raise FileNotFoundError("ollama CLI not found")

    def generate(self, prompt: str) -> str:
        candidates = [
            [self.exe, "run", self.model, prompt],
            [self.exe, "chat", self.model, prompt],
            [self.exe, "predict", self.model, prompt],
            [self.exe, "generate", self.model, prompt],
            [self.exe, "completion", self.model, prompt],
            [self.exe, "infer", self.model, prompt],
        ]
        errors = []
        for cmd in candidates:
            try:
                completed = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
            except FileNotFoundError:
                raise FileNotFoundError("ollama CLI not found")
            except Exception as e:
                errors.append(f"{cmd}: {e}")
                continue
            out = (completed.stdout or completed.stderr or '').strip()
            if completed.returncode == 0 and out:
                return out
            errors.append(f"{cmd} returned {completed.returncode}: {out}")
        raise RuntimeError("No working ollama CLI command found. Attempts:\n" + "\n".join(errors))
