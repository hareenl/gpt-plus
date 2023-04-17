import requests

url = "https://secure.runpod.io/fast-stable-diffusion"

try:
    response = requests.get(url)
    response.raise_for_status()   # raise an exception for 4XX and 5XX HTTP status codes
    print(response.text)
    # Extracting headers from the response
    headers = response.headers
    print(headers)

    # Extracting cookies from the response
    cookies = response.cookies
    print(cookies)

    # Extracting content from the response in binary format
    data = response.content
    print(data)

    # Extracting json data from the response
    json_data = response.json()
    print(json_data)

except requests.exceptions.ConnectionError as ce:
    print(f"Connection Error: {ce}")
except requests.exceptions.HTTPError as he:
    print(f"HTTP Error: {he}")
except Exception as e:
    print(f"Error: {e}")