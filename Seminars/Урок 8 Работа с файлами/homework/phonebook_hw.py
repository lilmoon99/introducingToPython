import sqlite3 as sl

with sl.connect("phonebook_db.db") as con:
    cur = con.cursor()


def create_table():  # creating table
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


def add_new_contact():  # adding contact to tables 'contacts' and 'numbers'
    name = input("Имя: ")
    surname = input("Фамилия: ")
    phone = input("Номер телефона: ")
    cur.execute(f"INSERT INTO contacts VALUES('{name}','{surname}')")
    con.commit()
    last_row_id = cur.lastrowid
    cur.execute(f"INSERT INTO numbers(user_id,phone_number) VALUES('{last_row_id}','{phone}')")
    con.commit()

    while True:  # adding more numbers to last contact
        comm = int(input("""
        Хотите добавить ещё один номер?
        1 - Да
        2 - Нет
        """))
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


def search_by():
    print("""По какому параметру будем искать?
    1 - Имя
    2 - Фамилия
    3 - Номер""")
    commands = {1: 'name', 2: 'surname', 3: 'phone_number'}
    input_command = int(input())

    if commands.get(input_command) is None:
        print("Вы ввели неправильную команду!")
    else:
        search_arg = input(f"Введите {commands.get(input_command)}: ")
        if input_command == 1 or input_command == 2:
            cur.execute(f"""SELECT contacts.name, contacts.surname, numbers.phone_number
            FROM contacts
            JOIN numbers
            ON contacts.rowid = numbers.user_id
            WHERE contacts.{commands.get(input_command)} = "{search_arg}"
            """)
        elif input_command == 3:
            cur.execute(f"""SELECT 
            contacts.name, contacts.surname, numbers.phone_number
            FROM contacts
            JOIN numbers
            ON contacts.rowid = numbers.user_id
            WHERE numbers.{commands.get(input_command)} = {search_arg}
    """)
        row_count = 0
        for row in cur:
            row_count += 1
            print(row)
        if row_count == 0:
            print("Результат не найден")


create_table()
# add_new_contact()

while True:
    command = int(input("""
    1 - Добавить контакт
    2 - Показать всех
    3 - Поиск контакта
    Ваш выбор: """))
    if command == 1:
        add_new_contact()
    elif command == 2:
        show_all()
    elif command == 3:
        search_by()
    else:
        print("loser")
