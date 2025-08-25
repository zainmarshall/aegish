import os
import json

CONFIG_PATH = os.path.expanduser("~/.config/aegish.json")


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


def configure_system_prompt():
    BOLD = '\033[1m'
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    YELLOW = '\033[33m'

    config = load_config()
    print(f"\n{BOLD}{CYAN}=== System Prompt Configuration ==={RESET}")
    print(f"{YELLOW}What do you want to do? Press the corresponding number{RESET}")
    print(f"{BOLD}1.{RESET} Change System Prompt")
    print(f"{BOLD}2.{RESET} Reset System Prompt to default")

    while True:
        
        choice = (input(f"{BOLD}Choice (1/2){RESET}: ") or '').strip()
        if choice in ('1', '2'):
            break
        print(f"{YELLOW}Invalid choice. Please enter 1 or 2.{RESET}")

    if choice == '1':
        # change the system prompt in the json
        prompt = input(f"{BOLD}Enter the new system prompt:{RESET} ")
        config['system_prompt'] = prompt
        save_config(config)
        print(f"{GREEN}✔ System prompt updated successfully.{RESET}")
    else:
        # remove the system prompt from the config file to reset to default
        config.pop('system_prompt', None)
        save_config(config)
        print(f"{GREEN}✔ System prompt reset to default.{RESET}")