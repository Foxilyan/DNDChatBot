import telebot
from Dice.Dice import Dice
import json
import os
from Registrator import Registrator

with open('token.txt') as f:
    TOKEN = f.readline()

bot = telebot.TeleBot(TOKEN)

empty_sheet = {
    'bio': {
        'имя': None
    },
    'статы': {
        'сила': None,
        'ловкость': None,
        'телосложение': None,
        'интеллект': None,
        'мудрость': None,
        'харизма': None
    },
    'спасброски': {
        'спас сила': None,
        'спас ловкость': None,
        'спас телосложение': None,
        'спас интеллект': None,
        'спас мудрость': None,
        'спас харизма': None
    },
    'скиллы': {
        'акробатика': None,
        'расследование': None,
        'атлетика': None,
        'восприятие': None,
        'выживание': None,
        'выступление': None,
        'запугивание': None,
        'история': None,
        'ловкость рук': None,
        'магия': None,
        'медицина': None,
        'обман': None,
        'природа': None,
        'проницательность': None,
        'религия': None,
        'скрытность': None,
        'убеждение': None,
        'уход за животными': None
    }
}


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
def register(message):
    Registrator.start_register(message, bot)


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
                    bot.send_message(message.chat.id, f'{i}: {character[i]}')
                return
    bot.send_message(message.chat.id, 'Персонаж не найден')


associations = {}

@bot.message_handler(commands=['play_as'])
def associate_char_and_player(message):
    msg = message.text.split(' ')
    if len(msg) == 1:
        bot.send_message(message.chat.id, 'Введите команду вместе с именем персонажа')
        return
    name = " ".join(msg[1:])
    for file_name in os.listdir('../Characters'):
        if name == file_name[:-5]:
            with open(f'../Characters/{file_name}') as file:
                associations[message.from_user.id] = json.load(file)
                bot.send_message(message.chat.id, f'Игрок {message.from_user.first_name} играет как {name}')
                bot.send_message(message.chat.id, str(associations))
                return
    bot.send_message(message.chat.id, 'Персонаж не найден')


bot.infinity_polling()
