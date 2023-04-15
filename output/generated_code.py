import requests
import json

# Replace YOUR_API_KEY with your own OpenAI API key
api_key = 'YOUR_API_KEY'

# Set the API endpoint URL
url = 'https://api.openai.com/v1/images/generations'

# Set the prompt for generating the image
prompt = "an armchair in the shape of an avocado"

# Set the model to use. You can use either "image-alpha-001" or "image-beta-001"
model = "image-alpha-001"

# Set the response format to JSON
headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {api_key}'}

# Set the request payload
data = {
    'model': model,
    'prompt': prompt,
    'num_images': 1,  # Set the number of images to generate
    'size': '1024x1024',  # Set the size of the final image
    'response_format': 'url'  # Set the response format to URL
}

try:
    # Send the API request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Get the response URL
    json_response = response.json()
    
    if 'data' in json_response:
        image_url = json_response['data'][0]['url']
        print(f"DALL·E generated image URL: {image_url}")
    else:
        print("An error has occurred. Please try again later.")
        
except Exception as e:
    print(f"An error has occurred: {e}")