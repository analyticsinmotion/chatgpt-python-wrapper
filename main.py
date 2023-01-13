#######################################################################################################################
# Filename: main.py
# Creation Date: 4/01/2023
# Tested on: Python 3.11
# PEP8 Exceptions: NONE
# Description:  This is the main file that controls the execution of the python wrappers for accessing ChatGPT. It
#               imports the chatgpt_text, chat_gpt_images modules and allows users to what they want to do.
#
#######################################################################################################################

# Import json
import json

# Import files that contain the python wrappers for text and images
from chatgpt_text import chatgpt_text
from chatgpt_images import chatgpt_images


def menu():
    menu_options = {
        1: 'ChatGPT Text functionality',
        2: 'ChatGPT Image Generation functionality',
        3: 'Exit'
    }

    for key in menu_options.keys():
        print(key, '--', menu_options[key])

    menu_option_input = int(input('Please select an option 1 to 3 from the menu above: '))

    # Check what choice was entered and act accordingly
    if menu_option_input == 1:
        option1()
    elif menu_option_input == 2:
        option2()
    elif menu_option_input == 3:
        print('Thanks you. Goodbye')
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 3.')


def option1():
    input_prompt = input("Enter your text/question/scenario: ")
    result = chatgpt_text(input_prompt, output_to_file=True)
    result_dict = json.loads(str(result))
    return print("Answer: " + result_dict['choices'][0]['text'].strip('\n'))


def option2():
    input_prompt = input("Enter a description of the image you would like created: ")
    chatgpt_images(input_prompt, n=1, output_to_file=True)


if __name__ == '__main__':
    menu()
