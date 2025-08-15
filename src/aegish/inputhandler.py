
import argparse
import sys
from aegish.config import load_config, save_config, configure_interactive, DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT


class InputHandler:

    # Fallback if not provided and json is broken
    # from config import DEFAULT_SYSTEM_PROMPT, DEFAULT_MODEL

    @staticmethod
    def get():

        # Flags
        parser = argparse.ArgumentParser(description="Converting natural language to linux prompts")
        parser.add_argument('text', nargs='*', help='The natural language command to convert')
        parser.add_argument('--system-prompt', default=None, help=f'System prompt to prepend to the user prompt (default: {DEFAULT_SYSTEM_PROMPT})')
        parser.add_argument('--print-only', action='store_true', help='Only print the generated command, do not run it')
        parser.add_argument('--no-safety', action='store_true', help='Disable safety checks on generated commands')
        parser.add_argument('--configure', action='store_true', help='Configure default model and system prompt')
        parser.add_argument('--model', default=None, help=f'Model to use (default: `{DEFAULT_MODEL})')
        args = parser.parse_args()

        # Enter interactive configuration mode
        if args.configure:
            configure_interactive(DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT)
            sys.exit(0)

        config = load_config()

        # Use config defaults if not provided
        if args.model is None:
                args.model = config.get('model', DEFAULT_MODEL)
        if args.system_prompt is None:
                args.system_prompt = config.get('system_prompt', DEFAULT_SYSTEM_PROMPT)

        user_prompt = ' '.join(args.text).strip() if args.text else sys.stdin.read().strip()
        if not user_prompt:
            print("No input provided. Usage: ag <command>", file=sys.stderr)
            sys.exit(1)

        return args, user_prompt
