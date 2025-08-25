
import argparse
import sys
from aegish.debug import set_debug


class InputHandler:

    @staticmethod
    def get():
        parser = argparse.ArgumentParser(description="Converting natural language to linux prompts")
        parser.add_argument('text', nargs=argparse.REMAINDER, help='The natural language command to convert.')
        parser.add_argument('-p', '--print-only', action='store_true', help='Only print the generated command, do not run it')
        parser.add_argument('-n', '--no-safety', action='store_true', help='Disable safety checks on generated commands')
        parser.add_argument('--configure', '--config', action='store_true', dest='configure', help='Configure provider and models')
        parser.add_argument('--configure_system_prompt', '--sys-prompt', action='store_true', dest='configure_system_prompt', help='Configure the system prompt')
        parser.add_argument('-d', '--debug', '--verbose', '-v', action='store_true', help='Enable verbose/debug output')
        args = parser.parse_args()

        # Enter configure mode if --configure
        if args.configure:
            from aegish.config import configure_interactive, configure_system_prompt
            try: 
                configure_interactive()
            except KeyboardInterrupt:
                print("\nquit")
                sys.exit(0)
            sys.exit(0)

        if args.configure_system_prompt:
            try:
                configure_system_prompt()
            except KeyboardInterrupt:
                print("\nquit")
                sys.exit(0)
        # Print debug messages if debug is selected
        set_debug(args.debug)

        # If the text is blank, with no text
        if not args.text:
            print("No input provided. Usage: ag <command> \n Use ag --help to view flags. \n Make sure you run ag --config before first usage", file=sys.stderr)
            sys.exit(1)

        user_prompt = ' '.join(args.text).strip() if args.text else sys.stdin.read().strip()
        return args, user_prompt
