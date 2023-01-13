# ChatGPT - Python wrapper
Python wrapper to access OpenAI's ChatGPT functionality.
<br /><br />

<!-- DESCRIPTION -->
## Description
This project contains a number of test scripts that provide access to OpenAI's ChatGPT models (text, image).
<br />
For the ChatGPT text function a user will be requested to enter their text prompt, question or scenario. The resulting answer will be output on the screen. In addition, the output_to_file flag can be changed to output the text prompt, question, scenario, ChatGPT response and associated metadata in a JSON file.
<br /><br />

<!-- GETTING STARTED -->
## Getting Started
### Dependencies
- Requires an OpenAI API Key
- Requires the following Modules:
    - os
    - json
    - openai (https://github.com/openai/openai-python)
    - dotenv (https://pypi.org/project/python-dotenv/)
    - re
    - requests
    - shutil
    - hashlib

### Installing
- Create an account and get API Key at https://chat.openai.com
- Add the API Key to the openai-credentials.env file

### Executing Program
- Run the main.py file
