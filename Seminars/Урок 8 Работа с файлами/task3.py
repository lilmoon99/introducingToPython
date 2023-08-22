from random import *
import json

phone_book = {"Дядя Петя": {"phone_numbers": [9998881234, 9997772233], "birth_day": "121276", "email": "mail@mail.ss"},
              "Тетя Песя": {"phone_numbers": [9998881444]}}

while True:
    command = input("Введите команду: ",)

    if command == "/contact":
        name = input("Введите имя нового контакта: ",)
        number0 = input("Введите 1й номер: ",)
        number1 = input("Введите 2й номер: ",)
        bith_day = input("Введите ДР: ",)
        mail = input("Введите email: ",)
        phone_book[name] = {"phone_numbers": [number0, number1], "birth_day": bith_day, "email": mail}