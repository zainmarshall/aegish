# A list of all the providers, models, and there api code names that aegish supports   
# Used in config.py
PROVIDERS = {
    "gemini": {
        "models": [
            {"api": "gemini-2.5-pro", "name": "Gemini 2.5 Pro"},
            {"api": "gemini-2.5-flash", "name": "Gemini 2.5 Flash"},
            {"api": "gemini-2.5-flash-lite", "name": "Gemini 2.5 Flash Lite"},
            {"api": "gemini-2.0-flash", "name": "Gemini 2.0 Flash"},
            {"api": "gemini-2.0-flash-lite", "name": "Gemini 2.0 Flash Lite"},
        ]
    },
    "claude": {
        "models": [
            {"api": "claude-opus-4-1-20250805", "name": "Claude Opus 4.1"},
            {"api": "claude-opus-4-20250514", "name": "Claude Opus 4"},
            {"api": "claude-sonnet-4-20250514", "name": "Claude Sonnet 4"},
            {"api": "claude-3-7-sonnet-20250219", "name": "Claude 3.7 Sonnet"},
            {
                "api": "claude-3-7-sonnet-latest",
                "name": "Claude 3.7 Sonnet (latest alias)",
            },
            {"api": "claude-3-5-haiku-20241022", "name": "Claude 3.5 Haiku"},
            {
                "api": "claude-3-5-haiku-latest",
                "name": "Claude 3.5 Haiku (latest alias)",
            },
            {"api": "claude-3-haiku-20240307", "name": "Claude 3 Haiku"},
        ]
    },
    "openai": {
        "api": "openai",
        "models": [
            {"api": "gpt-5-2025-08-07", "name": "GPT-5"},
            {"api": "gpt-5-mini-2025-08-07", "name": "GPT-5 Mini"},
            {"api": "gpt-5-nano-2025-08-07", "name": "GPT-5 Nano"},
            {"api": "gpt-4.1-2025-04-14", "name": "GPT-4.1"},
        ],
    },
    "ollama": {
        "models": [
            {
                "api": "deepseek-r1:1.5b",
                "name": "DeepSeek-R1 (1.5B)",
                "family": "deepseek",
                "group": "deepseek-r1",
            },
            {
                "api": "deepseek-r1:7b",
                "name": "DeepSeek-R1 (7B)",
                "family": "deepseek",
                "group": "deepseek-r1",
            },
            {
                "api": "deepseek-r1:8b",
                "name": "DeepSeek-R1 (8B)",
                "family": "deepseek",
                "group": "deepseek-r1",
            },
            {
                "api": "deepseek-r1:14b",
                "name": "DeepSeek-R1 (14B)",
                "family": "deepseek",
                "group": "deepseek-r1",
            },
            {
                "api": "deepseek-r1:32b",
                "name": "DeepSeek-R1 (32B)",
                "family": "deepseek",
                "group": "deepseek-r1",
            },
            {
                "api": "deepseek-r1:70b",
                "name": "DeepSeek-R1 (70B)",
                "family": "deepseek",
                "group": "deepseek-r1",
            },
            {
                "api": "deepseek-r1:671b",
                "name": "DeepSeek-R1 (671B)",
                "family": "deepseek",
                "group": "deepseek-r1",
            },
            {
                "api": "gemma2:2b",
                "name": "Gemma 2 (2B)",
                "family": "gemma",
                "group": "gemma2",
            },
            {
                "api": "gemma2:9b",
                "name": "Gemma 2 (9B)",
                "family": "gemma",
                "group": "gemma2",
            },
            {
                "api": "gemma2:27b",
                "name": "Gemma 2 (27B)",
                "family": "gemma",
                "group": "gemma2",
            },
            {
                "api": "gemma:2b",
                "name": "Gemma (Gemma 1.1) (2B)",
                "family": "gemma",
                "group": "gemma1",
            },
            {
                "api": "gemma:7b",
                "name": "Gemma (Gemma 1.1) (7B)",
                "family": "gemma",
                "group": "gemma1",
            },
            {
                "api": "llama3.3:70b",
                "name": "Llama 3.3 (70B)",
                "family": "llama",
                "group": "llama3.3",
            },
            {
                "api": "smollm:135m",
                "name": "SmolLM (135M)",
                "family": "smollm",
                "group": "smollm",
            },
            {
                "api": "smollm:360m",
                "name": "SmolLM (360M)",
                "family": "smollm",
                "group": "smollm",
            },
            {
                "api": "smollm:1.7b",
                "name": "SmolLM (1.7B)",
                "family": "smollm",
                "group": "smollm",
            },
            {
                "api": "dolphin-llama3:8b",
                "name": "Dolphin-Llama3 (8B)",
                "family": "dolphin",
                "group": "dolphin-llama3",
            },
            {
                "api": "dolphin-llama3:70b",
                "name": "Dolphin-Llama3 (70B)",
                "family": "dolphin",
                "group": "dolphin-llama3",
            },
            {
                "api": "hermes3:3b",
                "name": "Hermes 3 (3B)",
                "family": "hermes",
                "group": "hermes3",
            },
            {
                "api": "hermes3:8b",
                "name": "Hermes 3 (8B)",
                "family": "hermes",
                "group": "hermes3",
            },
            {
                "api": "hermes3:70b",
                "name": "Hermes 3 (70B)",
                "family": "hermes",
                "group": "hermes3",
            },
            {
                "api": "hermes3:405b",
                "name": "Hermes 3 (405B)",
                "family": "hermes",
                "group": "hermes3",
            },
            {
                "api": "falcon3:1b",
                "name": "Falcon3 (1B)",
                "family": "falcon3",
                "group": "falcon3",
            },
            {
                "api": "falcon3:3b",
                "name": "Falcon3 (3B)",
                "family": "falcon3",
                "group": "falcon3",
            },
            {
                "api": "falcon3:7b",
                "name": "Falcon3 (7B)",
                "family": "falcon3",
                "group": "falcon3",
            },
            {
                "api": "falcon3:10b",
                "name": "Falcon3 (10B)",
                "family": "falcon3",
                "group": "falcon3",
            },
            {
                "api": "qwen3-coder:30b",
                "name": "Qwen3-Coder (30B)",
                "family": "qwen",
                "group": "qwen3-coder",
            },
            {
                "api": "qwen3-coder:480b",
                "name": "Qwen3-Coder (480B)",
                "family": "qwen",
                "group": "qwen3-coder",
            },
        ]
    },
}
