#######################################################################################################################
# Filename: main.py
# Creation Date: 4/01/2023
# Tested on: Python 3.11
# PEP8 Exceptions: NONE
# Description:  This is the main file that controls the execution of the python wrappers for accessing ChatGPT. It
#               imports the chatgpt_text module and allows users to ask a question.
#
#######################################################################################################################

# Import json
import json

# Import files that contain the python wrappers for text and images
from chatgpt_text import chatgpt_text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    question = input("Enter your question: ")
    result = chatgpt_text(question, output_to_file=True)
    result_dict = json.loads(str(result))
    print("Answer: " + result_dict['choices'][0]['text'].strip('\n'))
