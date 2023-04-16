import requests
import json
import base64

#Enter your OpenAI API key
api_key = "ENTER_YOUR_API_KEY_HERE"

#Create headers dictionary with API key for authorization
headers = {
    'Authorization': 'Bearer {}'.format(api_key)
}

#Enter the prompt for the image you want to generate
prompt = "a cat sitting on a cloud above the city at night"

#Enter the model you want to use (e.g. 'image-alpha-001' or 'image-beta-001')
model = "image-alpha-001"

#Enter the number of images you want generated (maximum is 10)
num_images = 1

#Enter the size of the image you want generated (e.g. '256x256', '512x512', or '1024x1024')
size = "512x512"

#Create data dictionary with prompt, model, number of images, and size
data = {
    "text": prompt,
    "model": model,
    "num_images": num_images,
    "size": size
}

try:
    #Send POST request to DALL·E API endpoint with data and headers
    response = requests.post('https://api.openai.com/v1/images/generations', json=data, headers=headers)

    #Decode image data from response
    response_data = json.loads(response.text)

    #If there is no data in the response dictionary
    if 'data' not in response_data:
        raise ValueError('Response did not contain any data.')
        
    #Get image URL
    image_url = response_data['data'][0]['url']

    #Decode image data from response
    image_binary = base64.b64decode(image_url.split(",")[1])

    #Save image to file
    with open("dalle_image.png", "wb") as f:
        f.write(image_binary)
        
except Exception as e:
    print('An error occurred:', e)