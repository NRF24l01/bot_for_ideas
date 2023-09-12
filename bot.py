import telebot
from telebot.apihelper import ApiTelegramException

from random import choice

from config import tele_token, keyboard_actions, help_txt

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

statuss = ['creator', 'administrator', 'member']

@bot.message_handler(commands=["start"])
def handle_start(message):
    if is_subscribed(message.from_user.id) in statuss:
        bot.send_message(message.from_user.id, "Вы подписаны на <a href='https://t.me/life_of_1561'>телеграм канал с новостями</a>", parse_mode="HTML")
    else:
        bot.send_message(message.from_user.id, parse_mode="HTML", text="Рекомендуем подписаться на <a href='https://t.me/life_of_1561'>канал с новостями</a>")

    loger.info(f"Get command /start('{message.text}') from @{message.from_user.username} id: {message.from_user.id}")
    key = Keyboa(items=keyboard_actions, front_marker="&action=", back_marker="$").keyboard
    bot.send_message(message.from_user.id, "Я - бот который помогает самоуправлению с идеями!",
                     reply_markup=dict_to_ReKeMa(keyboard_actions))
    bot.send_message(message.from_user.id, "Вот моё меню:", reply_markup=key)


@bot.message_handler(commands=["help"])
def handle_start(message):
    loger.info(f"Get command /help('{message.text}') from @{message.from_user.username} id: {message.from_user.id}")
    bot.send_message(message.from_user.id, help_txt)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    loger.info(f"Get message '{message.text}' from @{message.from_user.username} id: {message.from_user.id}")


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    received_callback = call.data
    print(received_callback)


@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
    loger.info(f"Get sticker '{message.sticker.file_id}' from @{message.from_user.username} id: {message.from_user.id}")


def is_subscribed(user_id):
    return bot.get_chat_member("-1001701856929", user_id).status


loger.info("Bot start")
# Запускаем бота
bot.polling(none_stop=True)
