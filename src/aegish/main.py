import sys

from aegish.gemini import GeminiHandler
from aegish.safetychecker import SafetyChecker
from aegish.inputhandler import InputHandler
from aegish.postprocess import PostProcessor
from aegish.commandrunner import CommandRunner
from aegish.ollama import OllamaHandler
from aegish.chatgpt import OpenAIHandler
from aegish.claude import ClaudeHandler
from aegish.config import load_config
from aegish.debug import print_debug



def main():
	# input
	args, user_prompt = InputHandler.get()

	config = load_config()
	provider = config.get('provider')
	
	# system prompt
	SYSTEM_PROMPT = "You are an expert Linux assistant. Convert the user's natural language request into a safe, correct Linux shell command. If the request is ambiguous or incomplete, infer the most helpful and complete command. For example, if the user says 'git commit', output 'git add . && git commit' to ensure all changes are included. Only output the command, and combine steps when it improves usability."
	prompt = f"{SYSTEM_PROMPT}\nUser: {user_prompt}"

	try:
		# Handle the ai providers
		handler = None
		response = None
		if(provider == 'gemini'):
			handler = GeminiHandler()
		elif(provider == 'ollama'):
			handler = OllamaHandler()
		elif(provider == 'openai'):
			handler = OpenAIHandler()
		elif(provider == 'claude'):
			handler = ClaudeHandler()
		else:
			raise ValueError(f"Unknown provider: {provider}")

		response = handler.generate(prompt)
		print_debug(f"Raw response from {provider}: {response}")

		command = PostProcessor.clean(response)

	except Exception as e:
		print(f"Provider error: {e}", file=sys.stderr)
		print(f"Have you run ag --config and saved your preferences? Aegish won't work until you have done so.")
		sys.exit(3)

	# Safety check
	if not args.no_safety and not SafetyChecker.confirm_and_run(command):
		sys.exit(0)

	# Prinot only should just only print
	if args.print_only:
		print(command)
		return

	# Run the command
	CommandRunner.run(command)



if __name__ == '__main__':
	main()
