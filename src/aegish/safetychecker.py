# Color Codes
BOLD = '\033[1m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[0m'

# Prompt the user with the ai's generated command and makes sure they want to run it. 
class SafetyChecker:
    @staticmethod
    def confirm_and_run(command: str) -> bool:
        print(f"{BOLD}{YELLOW}\nGenerated command:{RESET}", command)
        confirm = input(f"{BOLD}Press Enter to run, or type 'n' to cancel: {RESET}").strip().lower()
        if confirm and confirm != 'y':
            print(f"{RED}Command cancelled.{RESET}")
            return False
        return True
