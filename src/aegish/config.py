import os
import json

CONFIG_PATH = os.path.expanduser("~/.config/aegish.json")
DEFAULT_SYSTEM_PROMPT = "You are an expert Linux assistant. Convert the user's natural language request into a safe, correct Linux shell command. Only output the command. "
DEFAULT_MODEL = "phi3:mini"


def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=2)

def configure_interactive(default_model, default_system_prompt):
    config = load_config()
    BOLD = '\033[1m'
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    YELLOW = '\033[33m'


    print(f"\n{BOLD}{CYAN}=== aegish Configuration ==={RESET}")
    print(f"{YELLOW}You can set the default model and system prompt below.{RESET}")
    print(f"{YELLOW}Press Enter to keep the current value in brackets.{RESET}\n")

    current_model = config.get('model', default_model)
    current_prompt = config.get('system_prompt', default_system_prompt)

    model = input(f"{BOLD}Default model{RESET} [{current_model}]: ").strip() or current_model
    system_prompt = input(f"{BOLD}Default system prompt{RESET} [{current_prompt}]: ").strip() or current_prompt

    config['model'] = model
    config['system_prompt'] = system_prompt
    save_config(config)
    print(f"\n{GREEN}✔ Configuration saved successfully!{RESET}\n")
