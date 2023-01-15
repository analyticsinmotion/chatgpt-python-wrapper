#######################################################################################################################
# Filename: chatgpt_moderation.py
# Creation Date: 4/01/2023
# Tested on: Python 3.11
# PEP8 Exceptions: None
# Docstring format: Sphinx
# Description:  This is a test script that provides access to OpenAI's chatGPT model. It creates a function
#               chatgpt_moderation to check whether any user input violates OpenAI's content policy. Where a
#               violation is identified the user input should not be processed for the text completion or image
#               generation functions. The reason for the violation will be output on the screen. A full response can
#               also output as a JSON file that contains additional metadata.
#######################################################################################################################

# Import os, dotenv, openai, json, datetime
import os
from dotenv import load_dotenv
import openai
import json
from datetime import datetime


# Load the API key for OpenAI
load_dotenv('openai_credentials.env')
openai.api_key = os.getenv("OPENAI_API_KEY")


# Create a function to input text and set the moderation model
def chatgpt_moderation(prompt, model="text-moderation-stable", output_to_file=False):
    response_raw = openai.Moderation.create(input=prompt, model=model)

    # Convert the Completion response from an OpenAIObject to a dictionary type so can convert to JSON later
    response_raw_dict_all = response_raw.__dict__
    response_previous = response_raw_dict_all['_previous']
    response_ms = {key: response_raw_dict_all[key] for key in response_raw_dict_all.keys() & {'_response_ms'}}
    response_raw_dict = response_previous | response_ms

    # Create the UNIX EPOCH time as it is not generated in the moderation output like in completions or images
    unix_epoch_time_gmt = int(datetime.now().timestamp())
    # Create a dictionary for the UNIX EPOCH time so can convert to JSON later
    created_dict = {"created": unix_epoch_time_gmt}

    # Add the model runtime settings to a nested dictionary type so can convert to JSON later
    request_settings = {
        "parameters": [
            {
                "input": prompt,
                "model": model
            }
        ]
    }

    # Merge the two dictionaries together to form the amended response output
    response_dict = response_raw_dict | request_settings | created_dict

    # Convert response dictionary to valid JSON format with some PrettyPrint indent
    # response = json.dumps(response_dict, indent=4)

    # Output to JSON file using the ID as the filename
    if output_to_file is True:
        with open("output_chatgpt_moderation/" + response_raw['id'] + ".json", "w") as outfile:
            json.dump(response_dict, outfile, indent=4)

    # Get the violation status - does the input breach the OpenAI T&Cs - True means a breach.
    flagged_status = response_raw['results'][0]['flagged']
    if flagged_status is True:
        reason_categories_dict = response_raw['results'][0]['categories']
        breach_categories_list = [key for key, value in reason_categories_dict.items() if value is True]
        response_tuple = (True, breach_categories_list)
    else:
        response_tuple = (False, [])

    # Return the amended ChatGPT moderation details in JSON format
    return response_tuple
