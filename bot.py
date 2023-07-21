import telebot
from config import tele_token

bot = telebot.TeleBot(tele_token)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.text)

# Запускаем бота
bot.polling(none_stop=True)