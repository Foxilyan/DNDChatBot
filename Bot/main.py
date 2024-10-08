import telebot
from Dice.Dice import Dice

with open('token.txt') as f:
    TOKEN = f.readline()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['roll'])
def roll(message):
    msg_text = message.text.split(' ')
    if len(msg_text) == 1:
        size = 20
    else:
        size = int(msg_text[1])
    dice = Dice(size)
    bot.send_message(message.chat.id, dice.roll())


bot.infinity_polling()
