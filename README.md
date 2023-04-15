# gpt-plus
## _Multitasking ChatGPT with Bing functionality_

![](https://raw.githubusercontent.com/hareenl/gpt-plus/main/images/preview.gif)

## Features

- Automatic switching between ChatGPT and Bing depending on request
- Multitask mode to execute as many tasks as required with access to information acquired from a prior task.
- Multi-step Python code generation and creation of .py file as output'
- Multi-step HTML code generation and creation of .html file as output'
- Options for switching between gpt-3.5-turbo and gpt-4
- Text to speech support with AWS Polly (Neural Engine)
- Pre-built ChatGPT roles.
- Searching and scraping articles on Wikipeadia and google

## Options
Use the following options in gpt-plus for additional options:
```sh
Use 'tasks' to enter multitask mode.
Use 'read clipboard' to access text from clipboard.
Use 'import python' while in python developer role to import python files from input folder.
Use 'import html' to import html while in web developer role to import html files from the input folder.
Use 'ask gpt' to request response specifically from ChatGPT.
Use 'ask bing' to request response specifically from Bing.
Use 'search web' for searching the internet.
Use 'search wiki' for searching Wikipedia.
Use '!clear' to clear current history and move to a new topic.
Use '!reset' to clear history and reset program.
```
Additionally, gpt-plus will auto switch to Bing mode if in scenarios where ChatGPT is unable to access the latest information.


## Installation
Download gpt-plus and install dependencies.

```sh
git clone https://github.com/hareenl/gpt-plus.git
cd gpt-plus
pip3 install -r requirements.txt
```

## Configuration
Visit https://platform.openai.com/account/api-keys to generate a API Key
Add API key to .env file (hidden) located in the gpt-plus folder

#### Example
```sh
# .env
OPENAI_API_KEY=sk-abcdefghijklmnopqrstuvwxyz123456
```
### Optional Step - Bing
To add EdgeGPT functionality to gpt-plus, steps are as follows:
- Install the cookie editor extension for [Chrome/Edge](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
- Go to bing.com (Login to page)
- Open the extension
- Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
- Paste your cookies into a file cookies.json located in gpt-plus

Read additional details on [EdgeGPT](https://github.com/acheong08/EdgeGPT)

### Optional Step - AWS Polly
Add AWS Polly support for Text-to-Speech by filling in the AWS Access and Secret keys in the .env file.
If this step is completed, the console provide an option to enable Text-to-Speech when initialised.

#### Example
```sh
# .env
OPENAI_API_KEY=sk-abcdefghijklmnopqrstuvwxyz123456
AWS_ACCESS_KEY_ID=ABCDEFGHIJK123456
AWS_SECRET_ACCESS_KEY=abcdefghijklmnop1234
```

## Start gpt-plus

```sh
python3 gpt-plus.py
```

## Examples
### Multi step python code generation (Utilising Role 2: Python Developer)
![](https://raw.githubusercontent.com/hareenl/gpt-plus/main/images/preview1.png)
##### Code Output
The generated code is exported as 'generated_code.py' in the 'output' folder. Code below is based on above prompt input in Multitask mode.

```python
# Import the necessary libraries
import openai
import requests
import json

# Set up the API endpoint and token
openai.api_key = "<YOUR_API_KEY>"
endpoint = "https://api.openai.com/v1/images/generations"

# Take user input for the prompt generation
prompt_str = input("Enter a prompt to generate an image: ")

# Ask the user for image size selection
size_options = ["256x256", "512x512", "1024x1024"]
print("Choose an image size:")
for i, size_option in enumerate(size_options):
	print(f"{i+1}. {size_option}")
	
# Use a try-except block to handle errors if the user enters an invalid option
while True:
	try:
		size_index = int(input()) - 1
		size = size_options[size_index]
		break
	except:
		print("Invalid option. Please try again.")
		
# Set up the prompt generation parameters
model_engine = "davinci"
prompt = openai.Completion.create(
engine=model_engine,
prompt=prompt_str,
max_tokens=50,
n=1,
stop=None,
temperature=0.5
)

# Set the image parameters
model = "image-alpha-001"
prompt_text = prompt["choices"][0]["text"].strip()
response_format = "url"    # This will return a JSON object containing the URL of the generated image

# Set up the API request headers and body
headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {openai.api_key}"
}

data = {
"model": model,
"prompt": prompt_text,
"size": size,
"response_format": response_format
}

# Send the API request and print the result
try:
	response = requests.post(endpoint, headers=headers, data=json.dumps(data))
	response_dict = json.loads(response.text)
	print(response_dict["data"][0]["url"])
except:
	print("API request failed. Please try again.")
```

### Itinerary generation based on weather
![](https://raw.githubusercontent.com/hareenl/gpt-plus/main/images/preview2.png)

## Credits
- [EdgeGPT (Bing)](https://github.com/acheong08/EdgeGPT)
- [Prompthero (ChatGPT Prompts)](https://prompthero.com/chatgpt-prompts)
