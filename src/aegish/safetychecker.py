from typing import Tuple

class SafetyChecker:
    @staticmethod
    def confirm_and_run(command: str) -> bool:
        print("\033[1;33m\nGenerated command:\033[0m", command)
        confirm = input("\033[1mPress Enter to run, or type 'n' to cancel: \033[0m").strip().lower()
        if confirm and confirm != 'y':
            print("\033[31mCommand cancelled.\033[0m")
            return False
        return True
