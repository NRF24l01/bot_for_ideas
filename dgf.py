import psycopg2

conn = psycopg2.connect(dbname='botforideas', user='botforideas', password='Byq27ydb', host='31.31.192.187')
cursor = conn.cursor()
cursor.execute("select * from users")
print(cursor.fetchall())
cursor.close()  # закрываем курсор
conn.close()  # закрываем соединение
