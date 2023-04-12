# gpt-plus
## _Combination of ChatGPT and Bing with multi-tasking_

![](https://github.com/hareenl/gpt-plus/preview.gif)

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
Use 'tasks' to enter multi task mode.
Use 'read clipboard' to access text from clipboard.
Use 'ask gpt to request response specifically from ChatGPT.
Use 'ask bing' to request response specifically from bing.
Use '!reset' to reset program.
```
Additionally, gpt-plus will auto switch to bing mode if words such as 'weather' and 'news' are utilised in the prompt as ChatGPT doesn't have access to current information.


## Installation
Install the dependencies for gpt-plus.

```sh
git pull https://github.com/hareenl/gpt-plus.git
cd gpt-plus
pip3 install -r requirements.txt
```

Use the following to start gpt-plus

```sh
python3 gpt-plus.sh
```

## Configuration
Visit https://platform.openai.com/account/api-keys to generate a API Key
Add API key to .env file (hidden) located in the gpt-plus folder

Example

```sh
# .env
OPENAI_API_KEY=sk-abcdefghijklmnop123456
```

Next step is to add EdgeGPT functionality to gpt-plus. Steps are as follows:
- Install the cookie editor extension for [Edge](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)
- Go to bing.com (Login to page)
- Open the extension
- Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
- Paste your cookies into a file cookies.json located in gpt-plus

Read additional details on https://github.com/acheong08/EdgeGPT

## Credits
- EdgeGPT (Bing) - https://github.com/acheong08/EdgeGPT
- Prompthero (ChatGPT Prompts) - https://prompthero.com/chatgpt-prompts
