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
<br /><br />

<!-- INSTRUCTIONS -->
## Instructions

### Text Completion Example

Input Prompt:
```text
What are the top 5 emerging AI trends?
```
Response:
```text
1. Autonomous Vehicles: Autonomous vehicles are becoming increasingly popular and are expected to become a major part of the transportation landscape by 2023. Autonomous vehicles are expected to become commonplace in cities, allowing for faster and more efficient transportation.

2. Smart Cities: Smart cities are cities that use technology to improve the lives of their citizens. This includes things like self-driving cars, smart energy grids, and automated waste management systems.

3. AI-Powered Healthcare: AI-powered healthcare solutions are becoming more popular as they can help diagnose and treat illnesses more accurately and quickly. AI-powered healthcare solutions are expected to become more widespread in the next few years, allowing for more efficient and accurate healthcare.

4. Natural Language Processing: Natural language processing (NLP) is the ability of a computer to understand human language. NLP is becoming more popular and is being used in applications such as voice assistants and customer service chatbots.

5. Edge Computing: Edge computing is the use of computing resources that are located close to the user, such as on the user's device or in the cloud. Edge computing allows for faster and more efficient processing of data, which is becoming increasingly important as data becomes more complex.
```


### Image Generation Example

Input Prompt:
```text
landscape painting with water and trees
```
Response:

<img src="/output_chatgpt_images/images/img-hx959DWtE7QaZ8CWbSph0xo7.png" width=50% height=50%>
