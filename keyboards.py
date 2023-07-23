from telebot.types import ReplyKeyboardMarkup


def dict_to_ReKeMa(dictir: list[dict]):
    keyb = ReplyKeyboardMarkup()
    for i in dictir:
        keyb.add(i["text"])
    return keyb
