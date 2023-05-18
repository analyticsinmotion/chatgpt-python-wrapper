# ChatGPT – Python Wrapper
Python wrapper to access OpenAI's ChatGPT functionality.
<br /><br />
<!--
[![Analytics in Motion](https://raw.githubusercontent.com/analyticsinmotion/.github/main/assets/images/analytics-in-motion-github-badge-rectangle.svg)](https://www.analyticsinmotion.com)&nbsp;&nbsp;
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/release/python-3111/)&nbsp;&nbsp;
![Maintenance](https://img.shields.io/badge/Maintained-YES-green.svg?style=for-the-badge)&nbsp;&nbsp;
[![MIT license](https://img.shields.io/badge/License-MIT-orange.svg?style=for-the-badge)](https://mit-license.org/)&nbsp;&nbsp;
[![PEP8](https://img.shields.io/badge/code%20style-PEP8-green.svg?style=for-the-badge)](https://www.python.org/dev/peps/pep-0008/)&nbsp;&nbsp;
[![action](https://img.shields.io/badge/CodeQL-passing-green.svg?style=for-the-badge&logo=github&logoColor=959da4)](https://github.com/analyticsinmotion/chatgpt-python-wrapper/actions)
<br /><br />
-->

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg?style=badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/release/python-3111/)&nbsp;&nbsp;
[![PEP8](https://img.shields.io/badge/code%20style-PEP8-green.svg?style=badge)](https://www.python.org/dev/peps/pep-0008/)&nbsp;&nbsp;
[![MIT license](https://img.shields.io/badge/License-MIT-orange.svg?style=badge)](https://mit-license.org/)&nbsp;&nbsp;
[![action](https://img.shields.io/badge/CodeQL-passing-green.svg?style=badge&logo=github&logoColor=959da4)](https://github.com/analyticsinmotion/chatgpt-python-wrapper/actions)&nbsp;&nbsp;
[![Analytics in Motion](https://raw.githubusercontent.com/analyticsinmotion/.github/main/assets/images/analytics-in-motion-github-badge-rounded.svg)](https://www.analyticsinmotion.com)&nbsp;&nbsp;
<br /><br />

<!-- DESCRIPTION -->
## 1. Description
This project contains a number of test scripts that provide access to OpenAI's ChatGPT models (text, image).
### 1.1 ChatGPT Text Completions
For the ChatGPT text function a user will be requested to enter their text prompt, question or scenario. The resulting answer will be output on the screen. In addition, the output_to_file flag can be changed to output the text prompt, question, scenario, ChatGPT response and associated metadata in a JSON file.
### 1.2 ChatGPT Image Generator
For the ChatGPT image function a user will be requested to enter a description of the image they want created. The resulting image will be created and downloaded. In addition, the output_to_file flag can be changed to output the associated metadata in a JSON file.
### 1.3 ChatGPT Moderation
All user input will be analyzed to ensure it complies with [OpenAI's Content Policy](https://labs.openai.com/policies/content-policy). Any input that is flagged for hate, threats, self-harm, sexual, or violent will not be passed to our text completion or image generator functions. The output_to_file flag can be changed to output the associated metadata in a JSON file for all input requests, regardless of whether they are flagged as in violation or not.
<br /><br />

<!-- GETTING STARTED -->
## 2. Getting Started
### 2.1 Dependencies
- Requires an OpenAI API Key
- Requires the following Modules:
  - os (makes interaction with the local file system simpler)
  - json (in-built package to create, store, convert json objects)
  - openai (<a href="https://github.com/openai/openai-python">https://github.com/openai/openai-python</a>)
  - dotenv (<a href="https://pypi.org/project/python-dotenv/">https://pypi.org/project/python-dotenv/</a>)
  - re (to enable the use of regular expressions)
  - requests (to request images from the web)
  - shutil (to save images locally)
  - hashlib (create simple file IDs for images)
  
Please be aware of the [costs](https://openai.com/pricing) associated with using the OpenAI API when utilizing this project.

### 2.2 Installing
- Create an account and get API Key at <a href="https://chat.openai.com">https://chat.openai.com</a>
- Add the API Key to the openai-credentials.env file

### 2.3 Executing Program
- Run the main.py file
<br /><br />

<!-- DIRECTORY STRUCTURE -->
## 3. Directory Structure

    ChatGPT
    ├── output_chatgpt_images           # Directory
    │   ├── images                      # Directory
    ├── output_chatgpt_moderation       # Directory    
    ├── output_chatgpt_text             # Directory
    ├── chatgpt_images.py               # File
    ├── chatgpt_moderation.py           # File
    ├── chatgpt_text.py                 # File
    ├── main.py                         # File
    ├── openai_credentials.env          # File
    ├── LICENSE.md                      # File
    └── README.md                       # File
<br />

<!-- INSTRUCTIONS -->
## 4. Instructions

### 4.1 Text Completion Example

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


### 4.2 Image Generation Example

Input Prompt:
```text
landscape painting with water and trees
```
Response:

<img src="/output_chatgpt_images/images/img-hx959DWtE7QaZ8CWbSph0xo7.png" width=65% height=65%>
<br />


### 4.3 Moderation Example

Input Prompt:
```text
I want to kill them.
```
Response:
```text
(True, ['hate/threatening', 'violence'])
```
<br /><br />

<!-- JSON OUTPUT FILES -->
## 5. JSON Output Files (Optional)

### 5.1 Text Completion Example
Set the <b>output_to_file</b> flag to True in the chatgpt_text function in order to generate the a JSON output file for each request.
```text
chatgpt_text(prompt, output_to_file=True)
```
<br />

JSON Response:
```text
{
    "id": "cmpl-6WendmCVAliTTdQZCvh9MQBsrkin2",
    "object": "text_completion",
    "created": 1673241349,
    "model": "text-davinci-003",
    "choices": [
        {
            "text": "\n\nNo, Pluto is no longer considered a planet. It is now classified as a dwarf planet.",
            "index": 0,
            "logprobs": null,
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 5,
        "completion_tokens": 21,
        "total_tokens": 26
    },
    "parameters": [
        {
            "prompt": "Is Pluto a planet?",
            "max_tokens": 2048,
            "temperature": 0.5,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "n": 1
        }
    ]
}
```

### 5.2 Image Generation Example
Set the <b>output_to_file</b> flag to True in the chatgpt_images function in order to generate the a JSON output file for each request.
```text
chatgpt_images(prompt, output_to_file=True)
```
<br />

JSON Response:
```text
{
    "created": 1673589687,
    "data": [
        {
            "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-XXXXXXXXXXXXXXXXXXXXXXXX/user-XXXXXXXXXXXXXXXXXXXXXXXX/img-hx959DWtE7QaZ8CWbSph0xo7.png?st=2023-01-13T05%3A01%3A27Z&se=2023-01-13T07%3A01%3A27Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-01-13T00%3A13%3A40Z&ske=2023-01-14T00%3A13%3A40Z&sks=b&skv=2021-08-06&sig=nf9r9g20TYpxORNGKy3zT82atGsoAy/Q22sJrLTDKUE%3D"
        }
    ],
    "_response_ms": 5705,
    "parameters": [
        {
            "prompt": "landscape painting with water and trees",
            "size": "1024x1024",
            "n": 1
        }
    ],
    "ids": [
        "img-hx959DWtE7QaZ8CWbSph0xo7"
    ]
}
```


### 5.3 Moderation Example
Set the <b>output_to_file</b> flag to True in the chatgpt_moderation function in order to generate the a JSON output file for each request.
```text
chatgpt_moderation('I want to kill them.', output_to_file=True)
```
<br />

JSON Response:
```text
{
    "id": "modr-6Yu9h3Lz1mwNdfQLMmynkROTAynjF",
    "model": "text-moderation-001",
    "results": [
        {
            "categories": {
                "hate": false,
                "hate/threatening": true,
                "self-harm": false,
                "sexual": false,
                "sexual/minors": false,
                "violence": true,
                "violence/graphic": false
            },
            "category_scores": {
                "hate": 0.22702568769454956,
                "hate/threatening": 0.4133393466472626,
                "self-harm": 0.005232803523540497,
                "sexual": 0.01407555304467678,
                "sexual/minors": 0.0038546782452613115,
                "violence": 0.922382652759552,
                "violence/graphic": 0.036863770335912704
            },
            "flagged": true
        }
    ],
    "_response_ms": 136,
    "parameters": [
        {
            "input": "I want to kill them.",
            "model": "text-moderation-stable"
        }
    ],
    "created": 1673777034
}
```

<!-- Best Practices for API Key Safety -->
## 6. Best Practices for API Key Safety

Your OpenAI APIKEY key/s should be kept secure and private at all times.

Please follow the best practices guide for API security from OpenAI 
<br />
<a href="https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety">https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety</a>
