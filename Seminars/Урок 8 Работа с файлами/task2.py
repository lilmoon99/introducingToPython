import sqlite3 as sl

con = sl.connect("phonebook.db")

cur = con.cursor()


def create_table():
    cur.execute("""CREATE TABLE contact(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,surname text,phone_number text
    )""")
    con.commit()


def search_by():
    print("""По какому параметру будем искать?
    1 - Имя
    2 - Фамилия
    3 - Номер""")
    commands = {1: 'name', 2: 'surname', 3: 'phone_number'}
    input_command = int(input())
    search_arg = input(f"Введите {commands.get(input_command)}: ")
    cur.execute(f"select * from contact where {commands.get(input_command)} = '{search_arg}'")
    for row in cur.fetchall():
        print(row)


def show_data():  # показываем все записи таблицы users
    # commands = {1: 'name', 2: 'surname', 3: 'phone_number'}
    cur.execute("select * from contact")
    for row in cur.fetchall():
        print(row)


def add_into_empty():  # если таблица пустая то добавляется 2 записи
    cur.execute("select * from contact")
    if not cur.fetchall():
        cur.execute("INSERT INTO contact VALUES ('Айнур','Шамсуллин', 82489124)")
        con.commit()


def add_contact():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    phone = input("Номер телефона: ")
    cur.execute(f"INSERT INTO contact VALUES('{name}','{surname}','{phone}')")
    con.commit()


def delete_contact():
    print("""По какому параметру будем искать контакт для удаления?
    1 - Имя
    2 - Фамилия
    3 - Номер""")
    commands = {1: 'name', 2: 'surname', 3: 'phone_number'}
    input_command = int(input())
    delete_arg = input(f"Введите {commands.get(input_command)}: ")
    cur.execute(f"delete from contact where {commands.get(input_command)} = '{delete_arg}'")
    con.commit()


def delete_all():
    print("Привет разработчик!")
    cur.execute("delete from contact")
    con.commit()
    print("Все контакты успешно удалены!")


add_into_empty()
# show_data()
# add_contact()
# show_data()
# search_by()

while True:
    command = int(input("""
    1 - Добавить контакт
    2 - Посмотреть контакты
    3 - Поиск контакта
    4 - Удалить контакт
    5 - Выход из программы
    Ваш выбор: """))

    if command == 1:
        add_contact()
        print("Номер успешно добавлен")
    elif command == 2:
        show_data()
    elif command == 3:
        search_by()
    elif command == 4:
        delete_contact()
        print("Контакт успешно удалён!")
        # print("В разработке!")
    elif command == 5:
        print("До свидания!")
        break
    elif command == 999:
        delete_all()
    else:
        print("Вы ввели неправильную команду!")
