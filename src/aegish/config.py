DEFAULT_SYSTEM_PROMPT = "You are an expert Linux assistant. Convert the user's natural language request into a safe, correct Linux shell command. Only output the command. "
DEFAULT_MODEL = "phi3:mini"
import os
import json

CONFIG_PATH = os.path.expanduser("~/.config/aegish.json")


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
    print("\n--- aegish configuration ---")
    print("You can set the default model and system prompt here.")
    model = input(f"Default model (enter to leave unchanged)[{config.get('model', default_model)}]: ").strip() or config.get('model', default_model)
    system_prompt = input(f"Default system prompt (enter to leave unchanged) [{config.get('system_prompt', default_system_prompt)}]: ").strip() or config.get('system_prompt', default_system_prompt)
    config['model'] = model
    config['system_prompt'] = system_prompt
    save_config(config)
    print("Configuration saved.")
