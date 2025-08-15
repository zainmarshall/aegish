import subprocess
import sys

class CommandRunner:
    @staticmethod
    def run(command: str):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.stdout:
                print(result.stdout, end='')
            if result.stderr:
                print(result.stderr, end='', file=sys.stderr)
            if result.returncode != 0:
                print(f"[Command exited with code {result.returncode}]", file=sys.stderr)
        except Exception as e:
            print(f"[Error running command: {e}]", file=sys.stderr)
