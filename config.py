import telebot

stikers = ["CAACAgIAAxkBAAIG1WMwHKbXBXS7duSun6OY_xDSwh-4AAJvNwAC6VUFGEXj4pu7qah0KQQ", "CAACAgIAAxkBAAIFKGMvPElZ-4aLnfCFiY3pJtlUAe2wAAKHAgACVp29CkLtdCtAV9CQKQQ","CAACAgIAAxkBAAIFF2MvO_H1iGAkYZq5DaZGeUTsxvo5AAIRAgACVp29CpKL2lGpg2xbKQQ", "CAACAgIAAxkBAAIFn2MvQsXvIWlzsbNFQ_RJM7-SiWTPAAI0AQACUomRIxPN12_1HAdYKQQ", "CAACAgIAAxkBAAIFN2MvPPbGJErqYqxRqfdpumPmaCHOAAKEDAACxhrASOUL5dqyfqT_KQQ", "CAACAgIAAxkBAAIMgGNk_EB4KTlvcQ2m4VGhJQLL05amAALQIgACSZCZSv4i3O9H1JCHKgQ","CAACAgIAAxkBAAIMgWNk_EhT_sSHr2eIVKIxgbaxTtnHAAJlGAACuHRIS51TK_Qq-VnhKgQ","CAACAgIAAxkBAAIMgmNk_F13pRUV-2NjyNO1pSHPjxJGAALSFwAC1jMISCuxMuCieutrKgQ"]

db_name = "data.db"
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row("🆕предложить идею🆕")
keyboard1.row("👁️Посмотреть идеи👁️")
keyboard1.row("📛Правила📛", "🤜Профиль🤛")
keyboard1.row("☢️Разраб☢️", "🙋‍♂️Попасть в актив🙋‍♂️")

aktive_txt="""🙋‍♂️Попасть в актив🙋‍♂️
Всё просто:💁🏼‍♀️
Переходим в тг канал: 👉🏼https://t.me/life_of_1561
Тыкаем на закреп,🙌🏼
Пишем в коментарии и через некоторое время вас добавят.😉"""

rules_txt="""❗️ПРАВИЛА❗️
💥не спамить;
💥не материться;
💥четко формулировать идею, цели и желаемый результат. Желательно прописать необходимые ресурсы и количество человек для задачи;
💥вступать в актив только с абсолютной уверенностью в своих силах и ответственности.
💥Не нажимать на кнопки в момент после сообщения о приёме идеи
💥Не пресылать ничего плохого(Нарушаещего правила школы, УК РФ, Конституции
😉Я всё вижу в записях действий...🥸"""

creator_txt="""☢️Разраб☢️
Создатель: mcmeta
Класс: 6
Знаю языки: C++, Python, Xod, Scratch, не очень C# и Java.
Любимые игры: Minecraft Java Edition, KSP, Geometry Dash, Standoff 2
Любимые тг стикеры: https://t.me/addstickers/vk_anykey
Моя почта для вопросов: nevrovskiy.s@1561.ru
"""

help_txt="""❗️❗️Команды для админов❗️❗️
/ban - заблокировать пользователя (после команды указать ник) {пример: /ban tester1}
/deban - разблокировать пользователя (после команды указать ник) {пример: /deban tester1}
/del - удалить идею из списка (после команды указываете номер идеи) {пример: /del 1}
/complete - отметить идею как выполненую (после команды указываете номер идеи) {пример: /complite 1}
"""

versions = "[BETA 1.3]"