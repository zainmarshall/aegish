# aegish
Write linux commands in natural language using the power of local ai!

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Ollama Setup](#ollama-setup)
- [Development](#for-development-editable-install)

## Installation

### Install directly from GitHub

```
pip install git+https://github.com/zainmarshall/aegish.git
```

After installation, use the `ag` command:

```
ag --help
```

## Usage

Generate a Linux command from natural language:

```
ag list files in this directory
```

Print the generated command without running it:

```
ag --print-only show disk usage
```

Configure the default model and system prompt:

```
ag --configure
```

## Ollama Setup

This tool requires the [Ollama](https://ollama.com/) CLI to be installed and running locally.

1. Download and install Ollama from [ollama.com/download](https://ollama.com/download).
2. Make sure the `ollama` command is available in your PATH.
3. Start the Ollama server if it is not already running:
	```
	ollama serve
	```
4. (Optional) Download a model, e.g.:
	```
	ollama run phi3:mini
	```

You can set the model used by aegish with `--model` or in the configuration.


