
#!/usr/bin/env python3

import sys
from aegish.gemini import GeminiHandler
from aegish.safetychecker import SafetyChecker
from aegish.inputhandler import InputHandler
from aegish.postprocess import PostProcessor
from aegish.commandrunner import CommandRunner
from aegish.ollamahandler import OllamaHandler



def main():

	# input
	args, user_prompt = InputHandler.get()

	# system prompt is now hardcoded here
	SYSTEM_PROMPT = "You are an expert Linux assistant. Convert the user's natural language request into a safe, correct Linux shell command. If the request is ambiguous or incomplete, infer the most helpful and complete command. For example, if the user says 'git commit', output 'git add . && git commit' to ensure all changes are included. Only output the command, and combine steps when it improves usability."
	prompt = f"{SYSTEM_PROMPT}\nUser: {user_prompt}"

	gemini = True

	try:
		if gemini:
			gemini = GeminiHandler()
			response = gemini.generate(prompt)
			command = response.strip().split('\n', 1)[0].strip()
			command = PostProcessor.clean(command)
		else:
			ollama = OllamaHandler(args.model)
			response = ollama.generate(prompt)
		
	except Exception as e:
		print(f"Gemini error: {e}", file=sys.stderr)
		sys.exit(3)

	# Saftey
	if not args.no_safety:
		print("\033[1;33m\nCommand:\033[0m", command)
		confirm = input("\033[1mPress Enter to run, or type 'n' to cancel: \033[0m").strip().lower()
		if confirm and confirm != 'y':
			print("\033[31mCommand cancelled.\033[0m")
			sys.exit(0)

	# Prinot only should just only print
	if args.print_only:
		print(command)
		return

	# Run the command
	CommandRunner.run(command)



if __name__ == '__main__':
	main()
