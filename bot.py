import telebot

from config import tele_token, keyboard_actions

from logger import Logger
from time import time
from os import mkdir

from keyboards import dict_to_ReKeMa
from keyboa import Keyboa

bot = telebot.TeleBot(tele_token)
try:
    loger = Logger(f"log/{time()}.log")
except:
    mkdir("log")
    loger = Logger(f"log/{time()}.log")
loger.info("Loger start")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    loger.info(f"Get '{message.text}' from @{message.from_user.username}")
    key = Keyboa(
        items=keyboard_actions,
        front_marker="&action=",
        back_marker="$"
    ).keyboard
    bot.send_message(message.from_user.id, "адна КЛАВИАТУРА", reply_markup=key)
    bot.send_message(message.from_user.id, "втарая КЛАВИАТУРА", reply_markup=dict_to_ReKeMa(keyboard_actions))

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    received_callback = call.data
    print(received_callback)





loger.info("Bot start")
# Запускаем бота
bot.polling(none_stop=True)
