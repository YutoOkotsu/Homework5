# import sqlite3
# # sql - execute()-она выполняет команды sql
# # cursor()
# # база данных - таблица - поля
# db=sqlite3.connect('op37_3.db')
# c=db.cursor()
# c.execute('''CREATE TABLE IF NOT EXIST user(
# lastname TEXT,
# view INTEGER,
# nickname TEXT,
# age INTEGER
# ) ''')
# # insert into
# c.execuet('INSERT INTO user VALUES("")')
#
#
# # SELECT
# # fachallggggggg
# c.execute("SELECT lastname,age"

def create_connection(db_file):
    conn=False
    try:
        conn=sqliite3.connect(db_file)
    except Error:
        print(Error)

