import telebot
from Dice.Dice import Dice
import json
import os

with open('token.txt') as f:
    TOKEN = f.readline()

bot = telebot.TeleBot(TOKEN)
stats = ('имя', 'сила', 'ловкость', 'телосложение', 'интеллект', 'мудрость', 'харизма')


@bot.message_handler(commands=['roll'])
def roll(message):
    msg_text = message.text.split(' ')
    if len(msg_text) == 1:
        size = 20
    else:
        size = int(msg_text[1])
    dice = Dice(size)
    bot.send_message(message.chat.id, dice.roll())


@bot.message_handler(commands=['register'])
def start_register(message):
    character_sheet = {'stats': dict()}
    for stat in stats:
        bot.send_message(message.chat.id, f'Введите значение {stat}')
        bot.register_next_step_handler(message, register_stat, stat, character_sheet)
        while stat not in character_sheet.keys() and stat not in character_sheet['stats'].keys():
            pass

        if stat == 'имя':
            for file_name in os.listdir('../Characters'):
                if character_sheet[stat] in file_name:
                    bot.send_message(message.chat.id, f'Персонаж с таким именем уже существует')
                    return

    with open(f'../Characters/{character_sheet['имя']}.json', 'w', encoding='utf-8') as file:
        json.dump(character_sheet, file, indent=4)



def register_stat(message, stat, character_sheet):
    if stat == 'имя':
        character_sheet[stat] = message.text
    else:
        character_sheet['stats'][stat] = int(message.text)


@bot.message_handler(commands=['show'])
def show_character(message):
    msg = message.text.split(' ')
    if len(msg) == 1:
        bot.send_message(message.chat.id, 'Введите команду вместе с именем персонажа')
        return
    name = " ".join(msg[1:])
    for file_name in os.listdir('../Characters'):
        if name == file_name[:-5]:
            with open(f'../Characters/{file_name}') as file:
                character = json.load(file)
                for i in character:
                    if i == 'имя':
                        continue
                    bot.send_message(message.chat.id, f'{i}: {character[i]}')
                return
    bot.send_message(message.chat.id, 'Персонаж не найден')


bot.infinity_polling()
