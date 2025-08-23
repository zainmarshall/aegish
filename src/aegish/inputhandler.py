
import argparse
import sys
from aegish.config import configure_interactive
from aegish.debug import print_debug, set_debug


class InputHandler:

    @staticmethod
    def get():
        parser = argparse.ArgumentParser(description="Converting natural language to linux prompts")
        parser.add_argument('text', nargs='*', help='The natural language command to convert')
        parser.add_argument('--system-prompt', default=None, help='System prompt to prepend to the user prompt')
        parser.add_argument('--print-only', action='store_true', help='Only print the generated command, do not run it')
        parser.add_argument('--no-safety', action='store_true', help='Disable safety checks on generated commands')
        parser.add_argument('--configure', action='store_true', help='Configure aegish')
        parser.add_argument('--debug', action='store_true', help='Enable debug output')
        args = parser.parse_args()

        if args.configure:
            configure_interactive()
            sys.exit(0)

        set_debug(args.debug)

        user_prompt = ' '.join(args.text).strip() if args.text else sys.stdin.read().strip()
        if not user_prompt:
            print("No input provided. Usage: ag <command>", file=sys.stderr)
            sys.exit(1)

        return args, user_prompt
