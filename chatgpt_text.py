#######################################################################################################################
# Filename: chatgpt.py
# Creation Date: 4/01/2023
# Tested on: Python 3.11
# PEP8 Exceptions: None
# Docstring format: Sphinx
# Description:  This is a test script that provides access to OpenAI's chatGPT model. It creates a function chatgpt_text
#               that allows a users to enter a question and also adjust the model settings. The answer will be output
#               on the screen. A response can also output as a JSON file that contains additional metadata.
#######################################################################################################################

# Import os, dotenv, openai, json
import os
from dotenv import load_dotenv
import openai
import json


# Load the API key for OpenAI
load_dotenv('openai-credentials.env')
openai.api_key = os.getenv("OPENAI_API_KEY")


# Create a function to input text and set the model parameters
def chatgpt_text(prompt, model="text-davinci-003", max_tokens=2048, temperature=0.5, top_p=1, frequency_penalty=0,
                 presence_penalty=0, n=1, output_to_file=False):
    """
    This function passes the question/text to chatgpt and sets the model parameters

    :param prompt: the text to send to the model
    :param model: select one of the chatgpt models https://beta.openai.com/docs/models
    :param max_tokens: increase the max_tokens to generate more text
    :param temperature: increase the temperature to make the generated text more random. Higher values means the model
        will take more risks. Try 0.9 for more creative applications, and 0 for ones with a well-defined answer.
    :param top_p: An alternative to sampling with temperature, called nucleus sampling, where the model considers the
        results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10%
        probability mass are considered. https://beta.openai.com/docs/api-reference/completions/create
    :param frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing
        frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
        https://beta.openai.com/docs/api-reference/parameter-details
    :param presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they
        appear in the text so far, increasing the model's likelihood to talk about new topics.
        https://beta.openai.com/docs/api-reference/parameter-details
    :param n: How many completions to generate for each prompt
    :param output_to_file: output a JSON with the results

    :rtype: object
    """
    # Create a completion using the settings from function
    response_raw = openai.Completion.create(prompt=prompt, model=model, max_tokens=max_tokens, temperature=temperature,
                                            top_p=top_p, frequency_penalty=frequency_penalty,
                                            presence_penalty=presence_penalty, n=n)

    # Convert the Completion response from an OpenAIObject to a dictionary type so can convert to JSON later
    response_raw_dict = response_raw.__dict__['_previous']

    # Add the model runtime settings to a nested dictionary type so can convert to JSON later
    request_settings = {
        "parameters": [
            {
                "prompt": prompt,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "top_p": top_p,
                "frequency_penalty": frequency_penalty,
                "presence_penalty": presence_penalty,
                "n": n
            }
        ]
    }

    # Merge the two dictionaries together to form the amended response output
    response_dict = response_raw_dict | request_settings

    # Convert response dictionary to valid JSON format with some PrettyPrint indent
    response = json.dumps(response_dict, indent=4)

    # Output to JSON file using the ID as the filename
    if output_to_file is True:
        with open("output_chatgpt_text/"+response_raw['id']+".json", "w") as outfile:
            json.dump(response_dict, outfile, indent=4)

    # Return the amended chatGPT completion in JSON format
    return response
