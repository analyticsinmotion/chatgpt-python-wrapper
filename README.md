# ChatGPT - Python wrapper
Python wrapper to access OpenAI's ChatGPT functionality.
<br /><br />

<!-- DESCRIPTION -->
## Description
This project contains a number of test scripts that provide access to OpenAI's ChatGPT models (text, image).
### ChatGPT Text Completions
For the ChatGPT text function a user will be requested to enter their text prompt, question or scenario. The resulting answer will be output on the screen. In addition, the output_to_file flag can be changed to output the text prompt, question, scenario, ChatGPT response and associated metadata in a JSON file.
### ChatGPT Image Generator
For the ChatGPT image function a user will be requested to enter a description of the image they want created. The resulting image will be created and downloaded. In addition, the output_to_file flag can be changed to output the associated metadata in a JSON file.
<br /><br />

<!-- GETTING STARTED -->
## Getting Started
### Dependencies
- Requires an OpenAI API Key
- Requires the following Modules:
    - os (makes interaction with the local file system simpler)
    - json (in-built package to create, store, convert json objects)
    - openai (https://github.com/openai/openai-python)
    - dotenv (https://pypi.org/project/python-dotenv/)
    - re (to enable the use of regular expressions)
    - requests (to request images from the web)
    - shutil (to save images locally)
    - hashlib (create simple file IDs for images)

### Installing
- Create an account and get API Key at https://chat.openai.com
- Add the API Key to the openai-credentials.env file

### Executing Program
- Run the main.py file
