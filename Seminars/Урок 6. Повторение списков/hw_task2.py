# : Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]
from random import *
def init_list(length):
    start = int(input("Enter start point: "))
    finish = int(input("Enter finish point: "))
    return [randint(start,finish) for _ in range(length)]

def in_range(list,minimum,maximum):
    return [item for item in list if item > minimum and item < maximum]

list_1 = init_list(int(input("Enter a list length: ")))
print(list_1)
print(sorted(in_range(list_1,int(input("Enter min: ")),int(input("Enter max: ")))))