import sqlite3 as sl

con = sl.connect("gb.db")  # соединяемся с БД , если ее нету, то создаем такую БД

cur = con.cursor()


def create_table():
    # создаем пустую таблицу users со столбцами id, name, age если ее не было в БД
    cur.execute("""CREATE TABLE contact(
    name text,surname text,phone_number real
    )""")
    con.commit()  # сохраняем изменения


def show_data():  # показываем все записи таблицы users
    cur.execute("select * from users")
    for row in cur.fetchall():
        print(row)


def add_into_empty():  # если таблица пустая то добавляется 2 записи
    cur.execute("select * from users")
    if not cur.fetchall():
        cur.execute("INSERT INTO users (name,age) VALUES ('Иванов', 30)")
        con.commit()
        cur.execute("INSERT INTO users (name,age) VALUES ('Петров', 33)")
        con.commit()


create_table()
add_into_empty()
show_data()
