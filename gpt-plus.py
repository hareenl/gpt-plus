#!/usr/bin/env python3
import os
import re
import openai
import requests
import wikipedia
import pyperclip
import rollbar
from EdgeGPT import Chatbot, ConversationStyle
from googlesearch import search
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()
import asyncio


#API key for ChatGPT
openai.api_key = os.environ["OPENAI_API_KEY"]
model = "gpt-3.5-turbo"

def get_gpt_ver():
	print("\nPlease choose one of the following GPT models:")
	print("1. gpt-3.5-turbo")
	print("2. gpt-4")
	
	while True:
		try:
			choice = int(input("\nEnter the number of your choice: "))
			if choice in range(1, 3):
				break
			else:
				print("Invalid input. Please choose a number between 1 and 2.")
		except ValueError:
			print("Invalid input. Please enter a number.")
			
	ver = {
		1: "gpt-3.5-turbo",
		2: "gpt-4 (slow - Requires API access)"
	}
	
	with open("gptver.txt", "w") as file:
			# Write some text to the file
			file.write(ver[choice])
	return ver[choice]
			
			
def get_user_role():
	print("\nPlease choose one of the following roles:")
	print("1. General AI")
	print("2. Python Programmer")
	print("3. AI Image prompt generator")
	print("4. Legal Advisor")
	print("5. Screen writer")
	print("6. IT Expert")
	print("7. Financial Advisor")
	print("8. Novelist")
	print("9. Proofreader")
	print("10. Text based Game")
	
	while True:
		try:
			choice = int(input("\nEnter the number of your choice: "))
			if choice in range(1, 11):
				break
			else:
				print("Invalid input. Please choose a number between 1 and 10.")
		except ValueError:
			print("Invalid input. Please enter a number.")
	
	#Following ideas were for roles are from chatGPT propmpts on prompthero		
	roles = {
		1: "You are a helpful AI ready to assist with multiple tasks",
		2: "You are a programming assistant which outputs python code for given scenarios",
		3: "As a guide/prompter for a text-to-image AI, your task is to create a detailed prompt for the provided theme. The 'Prompt: ' should be concise, consisting of 5-10 short sentences that provide an initial description of the image, followed by the 'Keywords: ' , which are 5-10 descriptive adjectives or keywords to add depth and flavour. The 'Negative Words:' are the descriptive adjectives or keywords that you don't want included in the image. For example, if the prompt is 'A mighty dragon with gleaming scales taking flight over towering mountains in a dramatic display of power and grace.', you could add 'A mighty dragon', 'gleaming scales', towering mountains, 'dramatic as a Keywords and 'weak' or 'uninspiring' as a Negative Word, Please follow this exact pattern and do not make up your own",
		4: "I want you to act as my legal advisor. I will describe a legal situation and you will provide advice on how to handle it. You should only reply with your advice, and nothing else. Do not write explanations",
		5: "I want you to act as a screenwriter. You will develop an engaging and creative script for either a feature length film, or a Web Series that can captivate its viewers. Start with coming up with interesting characters, the setting of the story, dialogues between the characters etc. Once your character development is complete - create an exciting storyline filled with twists and turns that keeps the viewers in suspense until the end",
		6: "I want you to act as an IT Expert. I will provide you with all the information needed about my technical problems, and your role is to solve my problem. You should use your computer science, network infrastructure, and IT security knowledge to solve the problem. Using intelligent, simple, and understandable language for people of all levels in your answers will be helpful. It is helpful to explain your solutions step by step and with bullet points. Try to avoid too many technical details, but use them when necessary. Reply with the solution and do not write any explanations",
		7: "Provide guidance as an expertise on financial markets , incorporating factors such as inflation rate or return estimates along with tracking stock prices over lengthy period ultimately helping user understand sector then suggesting safest possible options available where he/she can allocate funds depending upon their requirement & interests",
		8: "I want you to act as a novelist. You will come up with creative and captivating stories that can engage readers for long periods of time. You may choose any genre such as fantasy, romance, historical fiction and so on - but the aim is to write something that has an outstanding plot-line, engaging characters and unexpected climaxes",
		9: "I want you act as a proofreader. I will provide you texts and I would like you to review them for any spelling, grammar, or punctuation errors. Once you have finished reviewing the text, provide me with any necessary corrections or suggestions for improve the text",
		10: "I want you to act as a text based adventure game. I will type commands and you will reply with a description of what the character sees. I want you to only reply with the game output and nothing else. do not write explanations. do not type commands unless I instruct you to do so. First command is wake up"
	}
	
	with open("role.txt", "w") as file:
			# Write some text to the file
			file.write(roles[choice])
	return roles[choice]

def tasks():
	# Ask the user to input a quantity of tasks
	while True:
		try:
			num_tasks = int(input("\nHow many tasks do you want to enter? "))
			if num_tasks in range(1, 100):
				break
			else:
				print("Invalid input. Please choose a number between 1 and 100.")
		except ValueError:
			print("Invalid input. Please enter a number.")
			
	
	
	# Create an empty list to store the tasks
	tasks = []
	
	# Request tasks from the user and add them to the list
	for i in range(num_tasks):
		task = input("Enter task {}: ".format(i+1))
		tasks.append(task)
	return tasks


async def bing(prompt):
	try:
		bing = Chatbot(cookiePath='cookies.json')
		response = await bing.ask(prompt=prompt, conversation_style=ConversationStyle.precise)
		
		if "item" not in response or "messages" not in response["item"]:
			print("Error: Invalid response format")
			return ""
		
		bot_messages = [message for message in response["item"]["messages"] if message["author"] == "bot"]
		
		if not bot_messages:
			print("Error: No bot messages found in response")
			return ""
		
		bing_response = bot_messages[-1]["text"]
		bing_response = re.sub('\[\^\d+\^\]', '', bing_response)
		print("\nBing:\n" + bing_response)
		return bing_response
	except Exception as e:
		print("Error:", str(e))
		return ""


def wiki(text):
	try:
		# Search for the term "Python"
		search_results = wikipedia.search(text)
		
		# Get the first search result and retrieve its summary and full content
		page = wikipedia.page(search_results[0])
		summary = page.summary
		
		# Print the summary and full content
		#print("Wikipedia Output:\n" + summary)
		
		# Write the summary to a file
		with open('wiki.txt', 'w') as f:
			f.write(summary)
	except wikipedia.exceptions.DisambiguationError as e:
		# Handle disambiguation error
		print(f"DisambiguationError: {e}")
	except wikipedia.exceptions.PageError as e:
		# Handle page not found error
		print(f"PageError: {e}")
	except Exception as e:
		# Handle other exceptions
		print(f"Error: {e}")
	return	
	
def google(query):
	try:
		results = list(search(query, tld="co.in", num=10, stop=10, pause=2))
		
		if not results:
			print("No results found.")
			return ""
		
		print('\n')
		for i, result in enumerate(results):
			print(i+1, result)
			
		while True:
			selection = input("\nSelect an option (1-10): ")
			
			try:
				selection = int(selection)
				if selection < 1 or selection > 10:
					print("Invalid selection. Please enter a number between 1 and 10.")
				else:
					# Get the selected search result
					selected_result = results[selection-1]
					print("Selected result:", selected_result)
					return selected_result
			except ValueError:
				print("Invalid input. Please enter a number between 1 and 10.")
	except Exception as e:
		# Handle any other exceptions
		print(f"Error: {e}")
		return ""

def previous_sesh():
	while True:
		response = input("\nHi, this is an improved version of ChatGPT with support for multiple roles, web scraping, google searching and executing multiple tasks. Complete the setup and use the following options: \nUse 'search web' for searching the internet.\nUse 'search wiki' for searching Wikipedia.\nUse 'tasks' to enter multi task mode.\nUse 'read clipboard' to access text from clipboard.\nUse 'ask gpt to request response specifically from ChatGPT.\nUse 'ask bing' to request response specifically from bing.\nUse '!reset' to reset program.\n\nWould you like to continue the previous session?:" + " (y/n) ").lower()
		if response in ["y", "yes"]:
			return True
		elif response in ["n", "no"]:
			with open('activity.txt', 'w') as f:
				# Add the text to the file
				f.write("")
			with open('web.txt', 'w') as f:
				# Add the text to the file
				f.write("")
			with open('role.txt', 'w') as f:
				# Add the text to the file
				f.write("")
			with open('wiki.txt', 'w') as f:
				# Add the text to the file
				f.write("")
			with open('gptver.txt', 'w') as f:
				# Add the text to the file
				f.write("")
			return False
		else:
			print("Invalid response. Please enter 'y' or 'n'.")
			

def contains_url(text):
	url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
	return bool(url_pattern.search(text))

def remove_url(text):
	url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
	return url_pattern.sub('', text)

def scrape_web(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			
			soup = BeautifulSoup(response.text, 'html.parser')
			# Get the title
			title = soup.find('title').text
			#print(f"Title: {title}")
			with open('web.txt', 'a') as f:
				# Add the text to the file
				f.write(title + '\n')
				
			# Get the article body
			article_body = soup.find('div', {'data-testid': ''})
			if article_body is not None:
				paragraphs = article_body.find_all('p')
				for paragraph in paragraphs:
					#print(paragraph.text)
					with open('web.txt', 'a') as f:
						# Add the text to the file
						f.write(paragraph.text)
			else:
				output = "Article body not found."
		else:
			output = "Failed to fetch the webpage."
	
	except requests.exceptions.ConnectionError as e:
		print("Error: ", e)				
		
def gpt(prompt, model, role):
	try:
		response = openai.ChatCompletion.create(
			max_tokens=1000,
			model=model,
			messages=[
				{"role": "system", "content": role },
				{"role": "user", "content": prompt},
			]
		)
		
		if not response or not response.choices:
			print("Error: Empty response from OpenAI")
			return ""
		
		result = ''
		for choice in response.choices:
			if choice.message and choice.message.content:
				result += choice.message.content
				
		if not result:
			print("Error: No content in response from OpenAI")
			return ""
		
		return result
	
	except Exception as e:
		rollbar.report_exc_info()
		print("Error asking ChatGPT:", str(e))
		return ""
	
def process_input(user_input, model, role):
	if	contains_url(user_input):
		url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
		url = url_pattern.findall(user_input)
		#print (url[0])
		scrape_web(url[0])
		with open('web.txt', 'r') as file:
			webtxt = file.read()# Use the previous role
			#print("Role: " + activity + "\n")	
		nourl = remove_url(user_input)
		
		if nourl is None:
			user_input = webtxt
		else:
			user_input = nourl + " " + webtxt
	
	if user_input.find('weather') != -1 or user_input.find('news') != -1 or user_input.find('price') != -1 or user_input.find('stock') != -1 or user_input.find('latest') != -1 or user_input.find('current') != -1:
		bing_input = user_input + ". Do not ask any questions after responding."
		user_input = asyncio.run(bing(bing_input))
		with open('activity.txt', 'w') as f:
			# Add the text to the file
			f.write(user_input+'\n')
		return 
	
	if user_input.find('ask bing') != -1:
		string_without_askbing = user_input.replace("ask bing", "") + ". Do not ask any questions after responding."
		user_input = asyncio.run(bing(string_without_askbing))
		with open('activity.txt', 'w') as f:
			# Add the text to the file
			f.write(user_input+'\n')
		return 
	
	if user_input.find('ask gpt') != -1:
		string_without_askbing = user_input.replace("ask gpt", "")
		user_input = asyncio.run(bing(string_without_askbing))
	
	
	if user_input.find('search wiki') != -1:
		string_without_wiki = user_input.replace("search wiki", "")
		wiki(str(string_without_wiki))
		with open('wiki.txt', 'r') as file:
			wikiout = file.read()# Use the previous role
			#print("Role: " + activity + "\n")
		user_input = "summarise" + wikiout
		
	if user_input.find('search web') != -1:
		string_without_search = user_input.replace("search web", "")
		#print(string_without_search)
		url = google(string_without_search)
		scrape_web(url)
		with open('web.txt', 'r') as file:
			webtxt = file.read()# Use the previous role
			#print("Role: " + activity + "\n")	
		user_input = "summarise" + webtxt
	
	if user_input.find('read clipboard') != -1:
		text = pyperclip.paste()
		string_without_clip = user_input.replace("read clipboard", "")
		user_input = string_without_clip + text
	
	if user_input == "shutdown":
		exit(0)
	if user_input == "!reset":
		with open('activity.txt', 'w') as f:
			# Add the text to the file
			f.write("")
		print('\n')
		main()
		
		
	with open('activity.txt', 'r') as file:
		activity = file.read()# Use the previous role
		#print("Role: " + activity + "\n")	
		
	user_input = activity + "\n" + user_input
	gptout = gpt(user_input,model,role)
	with open('activity.txt', 'w') as f:
		# Add the text to the file
		f.write(gptout+'\n')
	print('\nChatGPT:\n' + gptout)
	print('\n\n')

	
def main():
	
	if previous_sesh():
		with open('gptver.txt', 'r') as file:
			model = file.read()# Use the previous role
			#print("Role: " + activity + "\n")	
		with open('role.txt', 'r') as file:
			role = file.read()# Use the previous role
			#print("Role: " + activity + "\n")	
			
	else:
		with open('activity.txt', 'w') as f:
			# Add the text to the file
			f.write("")
		with open('web.txt', 'w') as f:
			# Add the text to the file
			f.write("")
			
		model = get_gpt_ver()
		role = get_user_role()	
	
			
	prompt_ = gpt("Describe given role in 25 words",model,role)
	print('\nChatGPT:\n' + prompt_)
		
	
	while True:
		user_input = input("\nInput: ")
		
		if user_input == "tasks":
			tasklist  = []
			tasklist = tasks()
			for i, task in enumerate(tasklist):
				print("\nProcessing task {}: {}".format(i+1, task))
				task = str(format(task))
				process_input(task, model, role)
				
		else:
			process_input(user_input, model, role)
main()