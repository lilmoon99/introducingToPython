from random import *
import json
films = []
def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")
    
def load():
        with open("films.json","r",encoding="utf-8") as fh:
            films = json.load(fh)
        print("Фильмотека была успешно загружена.")
        
try:
    with open("films.json","r",encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека была успешно загружена.")
except:
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин Колец")
    films.append("Техасская резня безнопилой")
    films.append("Санта Барбара")

while True:
    command= input("Введите команду: ")
    if command == "/start":
        print("Бот-фильмотека начал свою работу!")
    elif command == "/stop":
        print("Бот остановил свою работу. Заходите ещё, будем рады!")
        save()
        break
    elif command == "/all":
        print(f"Текущий список фильмов: {films}")
    elif command == "/add":
        f = (input("Введите название фильма: "))
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию.")
    elif command == "/help":
        print("Здесь какой-то мануал.")
    elif command == "/delete":
        f = input("Введите название фильма, который нужно удалить: ")
        if f in films:
            films.remove(f)
            print(f"{f} удален из фильмотеки.")
        else:
            print("В фильмотеке нет данного фильма.")
    elif command == "/random":
        print(f"Будем смотреть - {choice(films)}")
        
    elif command == "/save":
        save()
    elif command == "/load":
        load()
    else:
        print("Неопознанная команда. Просьба изучить мануал через /help.")
    