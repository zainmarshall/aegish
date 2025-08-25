
import argparse
import sys
from aegish.config import configure_interactive, configure_system_prompt
from aegish.debug import print_debug, set_debug


class InputHandler:

    @staticmethod
    def get():
        parser = argparse.ArgumentParser(description="Converting natural language to linux prompts")
        parser.add_argument('text', nargs='*', help='The natural language command to convert')
        parser.add_argument('--print-only', action='store_true', help='Only print the generated command, do not run it')
        parser.add_argument('--no-safety', action='store_true', help='Disable safety checks on generated commands')
        parser.add_argument('--configure', action='store_true', help='Configure aegish')
        parser.add_argument('--configure_system_prompt', action='store_true', help='Configure the system prompt which gives aegish context. Experiment with this to improve the utility of this tool. If you find a good system prompt, write a github issue and I will look into it :)')
        parser.add_argument('--debug', action='store_true', help='Enable debug output')
        args = parser.parse_args()

        # Enter configure mode if --configure
        if args.configure:
            configure_interactive()
            sys.exit(0)

        if args.configure_system_prompt:
            configure_system_prompt()
            sys.exit(0)
        # Print debug messages if debug is selected
        set_debug(args.debug)

        # If the text is blank, with no text
        if not args.text:
            print("No input provided. Usage: ag <command> \n Use ag --help to view flags. \n Make sure you run ag --config before first usage", file=sys.stderr)
            sys.exit(1)

        user_prompt = ' '.join(args.text).strip() if args.text else sys.stdin.read().strip()
        return args, user_prompt
