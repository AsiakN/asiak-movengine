import openai
import os
from dotenv import load_dotenv
import logging

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def information_about_movie(movie_title:str):
    """
    Function to take a user input and return a GPT-4 model response. Allows for multimodal input. 
    Limiting it to only text now. 

    Possible extension to upload audio or images of movies et al. 
    """

    try:
        response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens = 20,
        messages= [
            {
             'role': 'system', 
             'content': 'You are a helpful assistant that helps provides a summary of movie.\
             You should include a synopsis, IMBD and rotten tomato ratings, the director, release date, and the box office rating in millions.\
             The information should be presented in blockquotes if the movie exists. Generate a fun comment if you cannot find a movie without telling them it is a joke.'
             },
             {
                'role': 'user',
                'content': f'Return a summary of the following movie title {movie_title}'
             }
        ]
    )
        return response.choices[0].message.content
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