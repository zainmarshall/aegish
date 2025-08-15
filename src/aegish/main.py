
#!/usr/bin/env python3

import sys
from aegish.ollamahandler import OllamaHandler
from aegish.safetychecker import SafetyChecker
from aegish.inputhandler import InputHandler
from aegish.postprocess import PostProcessor
from aegish.commandrunner import CommandRunner



def main():
	args, user_prompt = InputHandler.get()
	system_prompt = args.system_prompt
	prompt = f"{system_prompt}\nUser: {user_prompt}"



	# Use OllamaClient
	try:
		ollama = OllamaHandler(args.model)
		response = ollama.generate(prompt)
		command = response.strip().split('\n', 1)[0].strip()
		command = PostProcessor.clean(command)
	except Exception as e:
		print(f"Ollama error: {e}", file=sys.stderr)
		sys.exit(3)

	# Interactive safety confirmation
	if not args.no_safety:
		print("\033[1;33m\nCommand:\033[0m", command)
		confirm = input("\033[1mPress Enter to run, or type 'n' to cancel: \033[0m").strip().lower()
		if confirm and confirm != 'y':
			print("\033[31mCommand cancelled.\033[0m")
			sys.exit(0)

	if args.print_only:
		print(command)
		return

	CommandRunner.run(command)



if __name__ == '__main__':
	main()
