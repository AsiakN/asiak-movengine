import os
import openai
from dotenv import load_dotenv
import requests

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_BASE_URL")

# models = openai.Model.list()

api_key = openai.api_key
api_url = openai.api_base

def create_emoji(prompt: str):
    header = {'Authorization' :f'Bearer {api_key}'}
    payload = {'model': 'text-davinci-002', 'prompt': prompt, "max_tokens": 6, "temperature": 0.9}
    response = requests.post(url=api_url, headers=header, data=payload)
    if response.status_code == 200: 
        return response
    return f"Something went wrong😶"

    

res = create_emoji("Iron man")