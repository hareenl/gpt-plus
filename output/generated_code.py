import openai

try:
    openai.api_key = "your key goes here" # replace this with your key
    def chat_gpt(prompt):
        model_engine = "davinci" # can be changed to any other GPT engine available
        response_length = 250 # max length of response
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=response_length
        )
        message = completions.choices[0].text.strip()
        return message

    text = input("Enter your message: ")
    print(chat_gpt(text))

except openai.error.AuthenticationError:
    print("Authentication error: Incorrect API key provided. You can find your API key at https://platform.openai.com/account/api-keys.")
except Exception as e:
    print(f"An error occurred: {e}")