
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

	# Safety check on output command
	if not args.no_safety:
		ok, reason = SafetyChecker.check(command)
		if not ok:
			print(f"Blocked by safety check (output): {reason}", file=sys.stderr)
			sys.exit(2)

	if args.print_only:
		print(command)
		return
	


	CommandRunner.run(command)



if __name__ == '__main__':
	main()
