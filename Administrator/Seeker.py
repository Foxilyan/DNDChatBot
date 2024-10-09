import os
import json


def get_name_from_command(message):
    msg = message.text.split(' ')
    if len(msg) == 1:
        return None
    return ' '.join(msg[1:])


def get_character(name, bot):
    for file_name in os.listdir('../Characters'):
        if name == file_name[:-5]:
            with open(f'../Characters/{file_name}') as file:
                character = json.load(file)
                return character
    return None