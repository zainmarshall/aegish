import os
import json

CONFIG_PATH = os.path.expanduser("~/.config/aegish.json")
DEFAULT_SYSTEM_PROMPT = (
    "You are an expert Linux assistant. Convert the user's natural language request into a safe, correct Linux shell command. "
    "If the request is ambiguous or incomplete, infer the most helpful and complete command. "
    "For example, if the user says 'git commit', output 'git add . && git commit' to ensure all changes are included. "
    "Only output the command, and combine steps when it improves usability."
)


def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    print("Please run 'ag --config'")
    return {}

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=2)


def configure_interactive():
    from aegish.models import PROVIDERS
    config = load_config()
    BOLD = '\033[1m'
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    YELLOW = '\033[33m'

    print(f"\n{BOLD}{CYAN}=== aegish Configuration ==={RESET}")
    print(f"{YELLOW}Select your provider, model, and API key if needed.{RESET}\n")

    # Provider selection
    provider_list = list(PROVIDERS.keys())
    for idx, name in enumerate(provider_list, 1):
        print(f"{idx}: {name.title()}")
    while True:
        try:
            provider_choice = int((input(f"{BOLD}Provider (number){RESET}: ") or '').strip())
            if 1 <= provider_choice <= len(provider_list):
                provider = provider_list[provider_choice - 1]
                break
        except ValueError:
            pass
        print(f"{YELLOW}Invalid choice. Please enter a number from the list.{RESET}")

    # Model selection (show available models)
    models = PROVIDERS[provider]["models"]
    print(f"{BOLD}Available models for {provider.title()}:{RESET}")
    for idx, m in enumerate(models, 1):
        print(f"  {idx}: {m['name']}")
    while True:
        try:
            model_choice = int((input(f"{BOLD}Model (number){RESET}: ") or '').strip())
            if 1 <= model_choice <= len(models):
                model = models[model_choice - 1]
                break
        except ValueError:
            pass
        print(f"{YELLOW}Invalid choice. Please enter a number from the list.{RESET}")

    # API Key (only for cloud providers)
    api_key = ''
    if provider in ('gemini', 'claude', 'openai'):
        api_key = (input(f"{BOLD}API Key for {provider.title()}{RESET}: ") or '').strip()

    config['provider'] = provider
    config['model'] = model
    if api_key:
        config['api_key'] = api_key
    else:
        config.pop('api_key', None)
    save_config(config)
    print(f"\n{GREEN}✔ Configuration saved successfully!{RESET}\n")
