from email import message
import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
import ollama
from sympy import principal_branch
from Website import Website

MODEL = "llama3.2"

#ed = Website("https://edwarddonner.com")
#print(ed.title)
#print(ed.text)

system_prompt = "You are an assistant that analyzes the contents of a website and provides a short summary, " \
"ignoring text that might be navigation related. Respond in markdown."

def messages_for(website):
    user_prompt = f"You are looking at a website titled {website.title}. The contents of this website is as follows; please provide a short summary of this website in markdown. If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

def summarize(url):
    website = Website(url)
    messages = messages_for(website)
    
    print(messages)
    
    print("-----------")

    response = ollama.chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)

summarize("https://edwarddonner.com")