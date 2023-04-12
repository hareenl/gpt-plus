# gpt-plus
## _Combination of ChatGPT and Bing with multi-tasking_


## Features

- Automatic switching between chatgpt and bing depending on request
- Multitask mode to execute as many tasks as required with access to information aquired from a prior task.
- Wikipeadia searching 
- Google Searching
- Ability to switch between gpt-3.5-turbo and gpt-4
- Options for switching between multiple chatgpt roles

## Options
Use the following options in gpt-plus for additional options:
```sh
Use 'search web' for searching the internet.
Use 'search wiki' for searching Wikipedia.
Use 'ask bing' for bing chat.
Use 'tasks' to enter multi task mode.
Use 'read clipboard' to access text from clipboard
Use '!reset' to reset program.
```
Additionally, gpt-plus will auto switch to bing mode if words such as 'weather' and 'news' are utilised in the prompt as ChatGPT doesn't have access to current information.

## Installation
Install the dependencies for gpt-plus.

```sh
git pull https://github.com/hareenl/gpt-plus
cd gpt-plus
pip3 install -r requirements.txt
```

Use the following to start gpt-plus

```sh
python3 gpt-plus.sh
```

## Credits
- EdgeGPT (Bing) - https://github.com/acheong08/EdgeGPT
- Prompthero (ChatGPT Prompts) - https://prompthero.com/chatgpt-prompts
