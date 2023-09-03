import sqlite3 as sl

with sl.connect("phonebook_db.db") as con:
    cur = con.cursor()


def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS contacts(
        name TEXT,
        surname TEXT
        )""")
    con.commit()
    cur.execute("""CREATE TABLE IF NOT EXISTS numbers(
        user_id INTEGER,
        number_id INTEGER  PRIMARY KEY AUTOINCREMENT,
        phone_number TEXT)""")
    con.commit()


def add_new_contact():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    phone = input("Номер телефона: ")
    cur.execute(f"INSERT INTO contacts VALUES('{name}','{surname}')")
    con.commit()
    last_row_id = cur.lastrowid
    cur.execute(f"INSERT INTO numbers(user_id,phone_number) VALUES('{last_row_id}','{phone}')")
    con.commit()
    while True:
        comm = int(input("""
        Хотите добавить ещё один номер?
        1 - Да
        2 - Нет"""))
        if comm == 1:
            phone = input("Номер телефона: ")
            cur.execute(f"INSERT INTO numbers(user_id,phone_number) VALUES('{last_row_id}','{phone}')")
            con.commit()
        elif comm == 2:
            break
        else:
            print("Вы ввели неправильную команду!")


def show_all():
    cur.execute("""SELECT contacts.name,contacts.surname,numbers.phone_number
    FROM contacts 
    JOIN numbers 
    ON contacts.rowid = numbers.user_id""")
    for row in cur.fetchall():
        print(row)


create_table()
# add_new_contact()

while True:
    command = int(input("""
    1 - Добавить контакт
    2 - Показать всех
    Ваш выбор: """))
    if command == 1:
        add_new_contact()
    elif command == 2:
        show_all()
    else:
        print("loser")
