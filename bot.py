import telebot
import config
import sqlite3
import random
from datetime import datetime
import ttoken

bot = telebot.TeleBot(ttoken.token)

@bot.message_handler(commands=["del"])
def like(message):
    pass

@bot.message_handler(commands=["del"])
def complite(message):
    log(message)
    current_datetime = str(datetime.now())
    resultee = current_datetime + " " + message.from_user.username + "  Use command: "+message.text
    print(resultee)
    if is_admin(message):
        us = extract_arg(message.text)
        deli(message, us[0])
        bot.send_message(message.chat.id, "Сделано.")
    else:
        bot.send_message(message.chat.id, "Вам не достаточно прав.")

@bot.message_handler(commands=["complete"])
def complite(message):
    log(message)
    current_datetime = str(datetime.now())
    resultee = current_datetime + " " + message.from_user.username + "  Use command: "+message.text
    print(resultee)
    if is_admin(message):
        us = extract_arg(message.text)
        comp(message, us[0])
        bot.send_message(message.chat.id, "Сделано.")
    else:
        bot.send_message(message.chat.id, "Вам не достаточно прав.")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, config.help_txt)
    log(message)
    current_datetime = str(datetime.now())
    resultee = current_datetime + " " + message.from_user.username + "  Use command: "+message.text
    print(resultee)

@bot.message_handler(commands=["ban"])
def ban(message):
    if is_admin(message):
        us = extract_arg(message.text)
        bun(message, us[0])
        bot.send_message(message.chat.id, "Сделано.")
    else:
        bot.send_message(message.chat.id, "Вам не достаточно прав.")
    log(message)
    current_datetime = str(datetime.now())
    resultee = current_datetime + " " + message.from_user.username + "  Use command: "+message.text
    print(resultee)


@bot.message_handler(commands=["op"])
def opi(message):
    if is_technik(message):
        us = extract_arg(message.text)
        op(message, us[0])
        bot.send_message(message.chat.id, "Сделано.")
    else:
        bot.send_message(message.chat.id, "Вам не достаточно прав.")
    log(message)
    current_datetime = str(datetime.now())
    resultee = current_datetime + " " + message.from_user.username + "  Use command: "+message.text
    print(resultee)

@bot.message_handler(commands=["deop"])
def opi(message):
    if is_technik(message):
        us = extract_arg(message.text)
        deop(message, us[0])
        bot.send_message(message.chat.id, "Сделано.")
    else:
        bot.send_message(message.chat.id, "Вам не достаточно прав.")
    log(message)
    current_datetime = str(datetime.now())
    resultee = current_datetime + " " + message.from_user.username + "  Use command: "+message.text
    print(resultee)

@bot.message_handler(commands=["deban"])
def deopi(message):
    if is_admin(message):
        us = extract_arg(message.text)
        debun(message, us[0])
        bot.send_message(message.chat.id, "Сделано.")
    else:
        bot.send_message(message.chat.id, "Вам не достаточно прав.")
    log(message)
    current_datetime = str(datetime.now())
    resultee = current_datetime + " " + message.from_user.username + "  Use command: "+message.text
    print(resultee)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    # ran_num = randint(0, 4)
    # stiker=config.stikers[ran_num]
    bot.send_sticker(m.chat.id, random.choice(config.stikers))
    bot.send_message(m.chat.id, 'Привет)) Я бот который помогает Самоуправлению ' + config.versions)
    bot.send_message(m.chat.id, '👇')

    # menu = [{'text': '🆕Предложить идею🆕', 'callback_data': 'new'}, {'text': '👁️Посмотреть идеи👁️', 'callback_data': 'watsh'}, ["📛Правила📛", "🫵Профиль🫵"], ["☢️Разраб☢️", "🙋‍♂️Попасть в актив🙋‍♂️"]]
    # keyboard = Keyboa(items=menu)

    bot.send_message(m.chat.id, 'Что Вы можете сделать?', reply_markup=config.keyboard1)
    user_id = m.from_user.username
    if not user_id:
        user_id = f"user_{random.randint(1, 1000)}"
    current_datetime = str(datetime.now())
    resultee = current_datetime + " " + user_id + " command: /start"
    print(resultee)
    new_y(m)
    log(m, "New")


@bot.message_handler(content_types=["sticker"])
def send_sticker(message):
    new_y(message)
    if is_user(message):
        # Получим ID Стикера
        sticker_id = message.sticker.file_id
        user_id = message.from_user.username
        current_datetime = datetime.now()
        if not user_id:
            user_id = f"user_{random.randint(1, 1000)}"
        resultee = str(current_datetime) + " " + user_id + " Send stiker: " + sticker_id
        log(message, "Отправил стикер: ")
        print(resultee)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    new_y(message)
    if is_user(message):
        if updstate(message, None) == "NONE":
            user_id = message.from_user.username
            current_datetime = str(datetime.now())
            if not user_id:
                user_id = f"user_{random.randint(1, 1000)}"
            resultee = current_datetime + " " + user_id + "  '" + message.text + "'"
            log(message, "Написал: ")
            print(resultee)
            if message.text == "🆕предложить идею🆕":
                new(message)
            elif message.text == "👁️Посмотреть идеи👁️":
                watch(message)
            elif message.text == "📛Правила📛":
                rules(message)
            elif message.text == "🤜Профиль🤛":
                profil(message)
            elif message.text == "☢️Разраб☢️":
                creator(message)
            elif message.text == "🙋‍♂️Попасть в актив🙋‍♂️":
                aktive(message)
        elif updstate(message, None) == "NEW":
            new_idea(message)
        is_admin(message)




def extract_arg(arg):
    return arg.split()[1:]

def new(message):
    bot.send_message(message.chat.id, '🖊Отправте идею🖊. "Нет" если не хотите оправлять.')
    global state
    updstate(message, True)
    # print(state)


def watch(message):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
        user = cursor.execute("SELECT COUNT(*) FROM users")
        # print(type(count))
        user_m = user.fetchall()
        user_t = user_m[0]
        # print(type(user_t))
        # print(type(user_m[0]))
        st = ""
        for item in user_t:
            st = st + str(item)
            # st = int(st)
        # bot.send_message(message.chat.id, 'Остальное дописывается')

        conn.commit()

    except sqlite3.Error as error:
        print("Error sql16: ", error)

    finally:
        if (conn):
            conn.close()
    st = ""
    for item in user_t:
        st = st + str(item)
        st = int(st)

    for i in range(1, st + 1):
        try:
            conn = sqlite3.connect(config.db_name)
            cursor = conn.cursor()

            # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
            idea = cursor.execute("SELECT idea FROM users WHERE id == " + str(i) + "").fetchall()[0][0]
            us_id = cursor.execute("SELECT us_id FROM users WHERE id == " + str(i) + "").fetchall()[0][0]
            user_id = cursor.execute("SELECT user_id FROM users WHERE id == " + str(i) + "").fetchall()[0][0]
            if idea.lower() != "нет":
                txt = f"""№ {str(i)}
Автор идеи: {us_id}/{user_id}
Текст идеи: {idea}"""
                bot.send_message(message.chat.id, txt)
            # bot.send_message(message.chat.id, 'Остальное дописывается')

            conn.commit()

        except sqlite3.Error as error:
            print("Error sql15: ", error)

        finally:
            if (conn):
                conn.close()


def rules(message):
    bot.send_message(message.chat.id, config.rules_txt)


def profil(message):
    prof(message)


def creator(message):
    bot.send_message(message.chat.id, config.creator_txt)


def aktive(message):
    bot.send_message(message.chat.id, config.aktive_txt)


def new_idea(message):
    if str(message.text.lower()) != "нет":
        try:
            conn = sqlite3.connect(config.db_name)
            cursor = conn.cursor()

            current_datetime = datetime.now()
            cursor.execute(
                "INSERT INTO 'users' (user_id, idea, us_id) VALUES ('" + str(message.from_user.username) + "', '" + str(
                    message.text) + "', '" + str(message.from_user.id) + "')")
            resultee = str(
                current_datetime) + " " + message.from_user.username + " Предложил новую идею: '" + message.text + "'"
            print(resultee)

            conn.commit()
        except sqlite3.Error as error:
            print("Error sql8: ", error)

        finally:
            if conn:
                conn.close()
        genPlus(message)
        log(message, "Предложил:")
        bot.send_message(message.chat.id, "Вы предложили идею: '" + message.text + "'")
    else:
        bot.send_message(message.chat.id, "Вы отменили отправку идеи")
        log(message, "Отменил отправку идеи:")
    updstate(message, False)

    # print(state)
    # log(message, "Предложил:")


def log(message, tylo = ""):
    if tylo == "Отправил стикер: ":
        try:
            conn = sqlite3.connect(config.db_name)
            cursor = conn.cursor()

            current_datetime = datetime.now()
            cursor.execute("INSERT INTO logs (user_id, time1, sob_type, sob, us_id) VALUES ('" + str(
                message.from_user.username) + "','" + str(
                current_datetime) + "', '" + tylo + "','" + message.sticker.file_id + "', '" + str(
                message.from_user.id) + "')")

            conn.commit()
        except sqlite3.Error as error:
            print("Error sql9: ", error)

        finally:
            if (conn):
                conn.close()
    elif tylo == "New":
        try:
            conn = sqlite3.connect(config.db_name)
            cursor = conn.cursor()

            current_datetime = datetime.now()
            cursor.execute("INSERT INTO logs (user_id, time1, sob_type, sob, us_id) VALUES ('" + str(
                message.from_user.username) + "','" + str(
                current_datetime) + "', 'решил запустить бота: ','" + message.text + "', '" + str(
                message.from_user.id) + "')")

            conn.commit()
        except sqlite3.Error as error:
            print("Error sql9: ", error)

        finally:
            if (conn):
                conn.close()
    else:
        try:
            conn = sqlite3.connect(config.db_name)
            cursor = conn.cursor()

            current_datetime = datetime.now()
            cursor.execute("INSERT INTO logs (user_id, time1, sob_type, sob, us_id) VALUES ('" + str(
                message.from_user.username) + "','" + str(
                current_datetime) + "', '" + tylo + "','" + message.text + "', '" + str(message.from_user.id) + "')")

            conn.commit()
        except sqlite3.Error as error:
            print("Error sql10: ", error)

        finally:
            if (conn):
                conn.close()


def new_used(message):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        current_datetime = datetime.now()
        cursor.execute(
            "INSERT INTO profiles (us_id, user_id, gener_ideas, non_rules, hz, compleat_ideas, status, dt_st) VALUES ('" + str(
                message.from_user.id) + "', '" + str(
                message.from_user.username) + "', '0', '0','109', '0', 'USER', 'NONE')")
        # cursor.execute("INSERT INTO profiles (compleat_ideas, status, dt_st) VALUES ('0', 'NONE', 'NONE')")
        # resultee = str(current_datetime) + " " + message.from_user.username + " Предложил новую идею: '" + message.text + "'"
        # print(resultee)

        conn.commit()
    except sqlite3.Error as error:
        print("Error sql11: ", error)

    finally:
        if (conn):
            conn.close()


def new_y(message):
    count_m = []
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
        count = cursor.execute("SELECT hz FROM profiles WHERE us_id == '" + str(message.from_user.id) + "'")
        # print(type(count))
        count_m = count.fetchall()

        conn.commit()

    except sqlite3.Error as error:
        print("Error sql12: ", error)

    finally:
        if (conn):
            conn.close()
    if len(count_m) == 0:
        new_used(message)


def updstate(message, st):
    global state, state_s
    if st == None:
        try:
            conn = sqlite3.connect(config.db_name)
            cursor = conn.cursor()

            # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
            state1 = cursor.execute("SELECT dt_st FROM profiles WHERE us_id == '" + str(message.from_user.id) + "'")
            # print(type(count))
            state_m = state1.fetchall()
            # print(type(count_m))
            state_pi = state_m[0]
            # print(type(count_pi))
            state_s = state_pi[0]
            # print(type(count_s))

            conn.commit()

        except sqlite3.Error as error:
            print("Error sql14: ", error)

        finally:
            if (conn):
                conn.close()
        return state_s
    elif st == True:
        try:
            conn = sqlite3.connect(config.db_name)
            cursor = conn.cursor()

            # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
            cursor.execute("UPDATE profiles SET dt_st = 'NEW' WHERE us_id == '" + str(message.from_user.id) + "'")
            # print(type(state_m), len(state_m))
            # state_pi = state_m[0]
            # print(type(state_pi), len(state_pi))
            # state_s = state_pi[0]
            # print(type(state_s), len(state_s))

            conn.commit()

        except sqlite3.Error as error:
            print("Error sql14: ", error)

        finally:
            if (conn):
                conn.close()
    elif st == False:
        try:
            conn = sqlite3.connect(config.db_name)
            cursor = conn.cursor()

            # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
            cursor.execute("UPDATE profiles SET dt_st = 'NONE' WHERE us_id == '" + str(message.from_user.id) + "'")

            conn.commit()

        except sqlite3.Error as error:
            print("Error sql14: ", error)

        finally:
            if (conn):
                conn.close()


def prof(message):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
        user = cursor.execute(
            "SELECT gener_ideas, non_rules, compleat_ideas, status FROM profiles WHERE us_id == " + str(
                message.from_user.id) + " ")
        # print(type(count))
        user_m = user.fetchall()
        # print(user_m, i)
        # print(user_m, user_m[0])
        user_t = user_m[0]
        st = ""
        conn.commit()

    except sqlite3.Error as error:
        print("Error sql16: ", error)

    finally:
        if (conn):
            conn.close()
    gen_idea = str(user_t[0])
    non_r = str(user_t[1])
    comp_id = str(user_t[2])
    state = str(user_t[3])
    us_id = str(message.from_user.id)

    txt = "Ваш id: " + us_id + """
""" + "📨Предложено идей Вами: " + gen_idea + """
""" + "🚫Нарушений: " + non_r + """
""" + "✅Сделано из преложеных Вами идей(твоих): " + comp_id + """
""" + "🙎‍♂️Ваш ранг: " + state

    bot.send_message(message.chat.id, txt)


def genPlus(message):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
        user = cursor.execute("SELECT gener_ideas FROM profiles WHERE us_id == " + str(message.from_user.id) + " ")
        # print(type(count))
        user_m = user.fetchall()
        # print(user_m, i)
        # print(user_m, user_m[0])
        user_t = user_m[0]
        # print(user_t, user_t[0])
        st = ""
        for item in user_t:
            st = st + str(item)
            # st = int(st)
        # bot.send_message(message.chat.id, 'Остальное дописывается')
        st = int(st)
        st = st + 1
        cursor.execute(
            "UPDATE profiles SET gener_ideas = " + str(st) + " WHERE us_id == '" + str(message.from_user.id) + "'")
        conn.commit()

    except sqlite3.Error as error:
        print("Error sql17: ", error)

    finally:
        if conn:
            conn.close()

def is_user(message):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
        user = cursor.execute("SELECT status FROM profiles WHERE us_id == "+str(message.from_user.id))
        user_m = user.fetchall()
        user_t = user_m[0]
        user_r = str(user_t[0])
        conn.commit()

    except sqlite3.Error as error:
        print("Error sql20: ", error)

    finally:
        if (conn):
            conn.close()
    if user_r == "BAN":
        return False
    else:
        return True

def bun(message, bunned):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        cursor.execute("UPDATE profiles SET status = 'BAN'  WHERE user_id == '" + str(bunned) + "'")

        conn.commit()

    except sqlite3.Error as error:
        print("Error21: ", error)

    finally:
        if (conn):
            conn.close()
    log(message, 'Забанил:' + str(bunned))

def debun(message, bunned):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        cursor.execute("UPDATE profiles SET status = 'USER'  WHERE user_id == '" + str(bunned) + "'")

        conn.commit()

    except sqlite3.Error as error:
        print("Error22: ", error)

    finally:
        if (conn):
            conn.close()
    log(message, 'Разбанил:' + str(bunned))

def is_admin(message):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        txt = cursor.execute("SELECT status FROM profiles WHERE us_id == " + str(message.from_user.id) + " ").fetchall()

        txt = str(txt[0][0])
        conn.commit()

    except sqlite3.Error as error:
        print("Error23: ", error)

    finally:
        if (conn):
            conn.close()
    if txt == "MOD" or txt == "TECHNIK":
        return True
    else:
        return False

def is_technik(message):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        txt = cursor.execute("SELECT status FROM profiles WHERE us_id == " + str(message.from_user.id) + " ").fetchall()

        txt = str(txt[0][0])
        conn.commit()

    except sqlite3.Error as error:
        print("Error24: ", error)

    finally:
        if (conn):
            conn.close()
    if txt == "TECHNIK":
        return True
    else:
        return False

def op(message, who):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        txt = cursor.execute("UPDATE profiles SET status = 'MOD'  WHERE user_id == '" + str(who) + "'")

        conn.commit()

    except sqlite3.Error as error:
        print("Error25: ", error)

    finally:
        if (conn):
            conn.close()
    log(message, 'Повысил' + str(who))

def deop(message, who):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        txt = cursor.execute("UPDATE profiles SET status = 'USER'  WHERE user_id == '" + str(who) + "'")

        conn.commit()

    except sqlite3.Error as error:
        print("Error26: ", error)

    finally:
        if (conn):
            conn.close()
    log(message, 'Разжаловал'+str(who))

def comp(message, id_of_idea):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET idea = 'Нет'  WHERE id == '" + str(id_of_idea) + "'")

        conn.commit()

    except sqlite3.Error as error:
        print("Error26: ", error)

    finally:
        if (conn):
            conn.close()

    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        id = cursor.execute("SELECT us_id FROM users WHERE id == " + str(id_of_idea) + " ").fetchall()[0][0]

        conn.commit()

    except sqlite3.Error as error:
        print("Error23: ", error)

    finally:
        if (conn):
            conn.close()

    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        new_count = cursor.execute(f"SELECT compleat_ideas FROM profiles WHERE us_id == '{id}'").fetchall()[0][0]

        conn.commit()

    except sqlite3.Error as error:
        print("Error23: ", error)

    finally:
        if (conn):
            conn.close()

    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        cursor.execute(f"UPDATE profiles SET compleat_ideas = '{new_count}'  WHERE us_id == '{str(id)}'")

        conn.commit()

    except sqlite3.Error as error:
        print("Error26: ", error)

    finally:
        if (conn):
            conn.close()

def deli(message, id):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET idea = 'Нет'  WHERE id == '" + str(id) + "'")

        conn.commit()

    except sqlite3.Error as error:
        print("Error26: ", error)

    finally:
        if (conn):
            conn.close()

def how_many_likes(message, idea_id):
    pass
# Запускаем бота
bot.polling(none_stop=True)