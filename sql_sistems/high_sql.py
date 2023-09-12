import sqlite3


def create_DB():
    # Create DB (embedded DBMS)
    conn = sqlite3.connect('tgbot2ver.susdatabase')
    c = conn.cursor()

    c.execute("""create table users(
       id INT NOT NULL,
       user_id VARCHAR (20) NOT NULL,
       user_name VARCHAR (20) NOT NULL,
       gen_ideas_count VARCHAR (50),
       warns_count VARCHAR (50),
       rang VARCHAR (50),
       dt_st VARCHAR (50),
       PRIMARY KEY (id)
    )""")

    c.execute("""
    create table ideas(
       id INT NOT NULL,
       user_id VARCHAR (20) NOT NULL,
       user_name VARCHAR (20) NOT NULL,
       idea_text TEXT,
       who_liked TEXT,
       PRIMARY KEY (id) )""")

    c.execute("""create table logs(
       id INT NOT NULL,
       user_id VARCHAR (20) NOT NULL,
       user_name VARCHAR (20) NOT NULL,
       do VARCHAR (50),
       dothat TEXT,
       PRIMARY KEY (id) )""")

    conn.commit()

    c.close()
    conn.close()

create_DB()
