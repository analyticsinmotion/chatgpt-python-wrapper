"""
This is a test script that provides access to OpenAI's ChatGPT model.
It creates a function chatgpt_images that allows a user to describe what image ChatGPT should create.
The image will be output in the output_chatgpt_images/images folder
A response can also be output as a JSON file that contains additional metadata.

Functions:
    chatgpt_images(prompt, n, size, output_to_file) -> object
"""
#######################################################################################################################
# Filename: chatgpt_images.py
# Creation Date: 4/01/2023
# Tested on: Python 3.11
# PEP8 Exceptions: None
# Docstring format: Sphinx
# Description:  This is a test script that provides access to OpenAI's chatGPT model. It creates a function
#               chatgpt_images that allows a users to enter what image it wants chatgpt to create. The image will be
#               output in the output_chatgpt_images/images folder. A response can also output as a JSON file
#               that contains additional metadata.
#######################################################################################################################

# Import os, dotenv, openai, json, re, requests, shutil, hashlib
import os
from dotenv import load_dotenv
import openai
import json
import re  # use regular expressions
import requests  # request images from the web
import shutil  # save images locally
import hashlib  # create simple file ids

# Load the API key for OpenAI
load_dotenv('openai_credentials.env')
openai.api_key = os.getenv("OPENAI_API_KEY")


# Create a function to input the image description and set the model parameters
def chatgpt_images(prompt, n=1, size="1024x1024", output_to_file=False):
    """
    This function passes the text prompt, question or scenario to chatgpt and sets the model parameters

    :param prompt: the text to send to the model
    :param n: How many completions to generate for each prompt
    :param size: The size of the generated images. Must be one of 256x256, 512x512, or 1024x1024
    :param output_to_file: output a JSON file with the results

    :rtype: object
    """

    # Create an image using the settings from function
    response_raw = openai.Image.create(prompt=prompt, n=n, size=size)

    # Initialise a blank list to capture all the image ids
    ids_list = []

    # Download the images
    for i in range(0, n):
        response_url = response_raw['data'][i]['url']
        # Extract the image ID from the URL the model creates
        re_id_pattern = r"(img-.*?)\.png"  # Get the image id
        re_file_pattern = r"img-.*?\.png"  # Get the full file name including image extension
        ids = re.findall(re_id_pattern, response_url)[0]  # Example output: 'img-YiVDiHbNylSFb1mN4Yc4Dgy'
        file_name = re.findall(re_file_pattern, response_url)[0]  # Example output: 'img-YiVDiHbNylSFb1mN4Yc4Dgy.png'
        ids_list.append(ids)  # Add the unique image id to a list as the loop iterates

        # Request the URL for downloading
        res = requests.get(response_url, stream=True)
        if res.status_code == 200:
            with open("output_chatgpt_images/images/" + file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image successfully Downloaded: ', file_name)
        else:
            print('Image could not be retrieved')

    # Convert the Completion response from an OpenAIObject to a dictionary type so can convert to JSON later
    response_raw_dict_all = response_raw.__dict__
    response_previous = response_raw_dict_all['_previous']
    response_ms = {key: response_raw_dict_all[key] for key in response_raw_dict_all.keys() & {'_response_ms'}}
    response_raw_dict = response_previous | response_ms

    # Add the model runtime settings to a nested dictionary type so can convert to JSON later
    request_settings = {
        "parameters": [
            {
                "prompt": prompt,
                "size": size,
                "n": n
            }
        ]
    }

    # Create a dictionary for the image ids. The number if ids is equal to n
    ids_dict = {'ids': ids_list}

    # Merge the three dictionaries together to form the amended response output
    response_dict = response_raw_dict | request_settings | ids_dict

    # Convert response dictionary to valid JSON format with some PrettyPrint indent
    response = json.dumps(response_dict, indent=4)

    # Create filename by hashing the image id/s and adding n as the final digit so can tell how many images requested
    # This was done as could not find a unique ID in the ChatGPT response for images
    file_name = str("img-" + hashlib.md5(" ".join(ids_list).encode()).hexdigest() + str("-") + str(n))

    # Output to JSON file
    if output_to_file is True:
        with open("output_chatgpt_images/" + file_name + ".json", "w") as outfile:
            json.dump(response_dict, outfile, indent=4)

    # Return the amended ChatGPT Image details in JSON format
    return response
