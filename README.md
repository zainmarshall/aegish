# aegish
Write linux commands in natural language using the power of local ai!

You can use aegish in two modes: Local or Cloud. Local uses ollama to run models on your device, whereas cloud uses your api key to make a request to a cloud provider.

Local providers: Ollama

Cloud Providers: ChatGPT (OpenAI), Gemini (Google), Claude (Anthropic) 



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)


## Installation

### Install directly from GitHub

```
pip install git+https://github.com/zainmarshall/aegish.git
```

After installation, use the `ag` configure command to choose local or cloud ai, to choose models, and to save api keys:

```
ag --configure
```

Make sure you know the api usage prices per model before selecting the model. The AI company will bill you based on usage and models used. 

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



