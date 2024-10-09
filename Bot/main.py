import telebot
from Dice.Dice import Dice
from Administrator import Registrator, Associator, Seeker

with open('token.txt') as f:
    TOKEN = f.readline()

bot = telebot.TeleBot(TOKEN)

associations = {}

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
    character = Seeker.get_character(Seeker.get_name_from_command(message), bot)
    if character is not None:
        for stats in character:
            bot.send_message(message.chat.id, f'{stats}: {character[stats]}')


@bot.message_handler(commands=['play_as'])
def associate_char_and_player(message):
    Associator.associate_char_and_player(message, bot, associations)


bot.infinity_polling()