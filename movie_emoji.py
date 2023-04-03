import os
import openai
from dotenv import load_dotenv
import logging

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# models = openai.Model.list()

api_key = openai.api_key

def create_emoji(movie_name: str):
    # print(api_key)
    # header = {'Authorization' :f'Bearer {api_key}'}
    # print(api_url)
    # payload = {'model': 'text-davinci-002', 'prompt': prompt, "max_tokens": 6, "temperature": 0.9}
    try:
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt= f'Remove the dates in the bracket in the movie title and convert the movie title to an emoji. \n\n{movie_name}',
        max_tokens=7,
        temperature=0.9
    )
        return response.choices[0].text
    except openai.error.APIError as e:
        print('failed to connect to api')
        logging.error(e._message)
    except openai.error.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass
    except openai.error.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass
    except openai.error.InvalidRequestError as e:
        #Handle invalid requests 
        print(f"OpenAI API invalid request: {e._message}")
        pass

    

# res = create_emoji("Iron Man 2 (2010)")
# print(res)