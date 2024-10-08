import telebot

with open('token.txt') as f:
    TOKEN = f.readline()

bot = telebot.TeleBot(TOKEN)





bot.infinity_polling()
