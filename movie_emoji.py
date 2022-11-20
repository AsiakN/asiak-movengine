import os
import openai
from dotenv import load_dotenv
import requests

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_BASE_URL")

models = openai.Model.list()

def create_emoji(prompt: str):
    header = {'Authorization' : openai.api_key}
    payload = {'model': 'text-davinci-002'}
    requests.post(openai.api_base, headers=header, params=)
    return None
