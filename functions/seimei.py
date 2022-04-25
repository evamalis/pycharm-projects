import telebot

TOKEN = "5334293748:AAFxSd_Ej6pBpIy_di7utBLwDvS80veKhJE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
   bot.reply_to(message, f"Welcome, {message.chat.username}")


@bot.message_handler(content_types=['photo', ])
def meme_reply(message: telebot.types.Message):
    bot.reply_to(message, f"Nice meme XDD")

@bot.message_handler(commands=['путин',])
def send_welcome(message: telebot.types.Message):
   bot.reply_to(message, f"хуйло")

@bot.message_handler(commands=['русский.корабль',])
def send_welcome(message: telebot.types.Message):
   bot.reply_to(message, f"иди нахуй")


bot.polling(none_stop=True)


