import sqlite3

try:
    conn = sqlite3.connect("dataNone.db")
    cursor = conn.cursor()

    txt = cursor.execute("SELECT user_id FROM profiles WHERE user_id='102423' ")


    conn.commit()

except sqlite3.Error as error:
    print("Error: ", error)

finally:
    if(conn):
        conn.close()