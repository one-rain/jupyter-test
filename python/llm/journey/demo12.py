from ollama import chat
from openai import OpenAI

openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

response = openai.chat.completions.create(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response)
# or access fields directly from the response object
print(response.choices[0].message.content)