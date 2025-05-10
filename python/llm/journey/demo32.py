import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
from PIL import Image

# 加载 .env 文件中的环境变量
load_dotenv(override=True)
deepseek_api_key = os.getenv('OPENAI_API_KEY')

if deepseek_api_key:
    print(f"DeepSeek API Key exists and begins {deepseek_api_key[:3]}")
else:
    print("DeepSeek API Key not set - please skip to the next section if you don't wish to try the DeepSeek API")

deepseek_client = OpenAI(
    api_key=deepseek_api_key, 
    base_url="https://api.deepseek.com"
)

system_message = "You are a helpful assistant for an Airline called FlightAI. "
system_message += "Give short, courteous answers, no more than 1 sentence. "
system_message += "Always be accurate. If you don't know the answer, say so."

MODEL=

def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = deepseek_client.chat.completions.create(model=MODEL, messages=messages)
    return response.choices[0].message.content

gr.ChatInterface(fn=chat, type="messages").launch()

