# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import *
def generator(length:int) -> list:
    temp_list = []
    for i in range(length):
        # temp_list.append(randint(1,10)) # filling list with random numbers
        temp_list.append(int(input(f"Введите {i+1} элемент набора: "))) # filling list one by one via printing
    return temp_list

def compare_lists(list1:list,list2:list) -> set:
    temp_set = set()
    for i in list1:
        for j in list2:
            if i == j:
                temp_set.add(i)
    temp_set = sorted(temp_set)
    return temp_set

list_1 = generator(int(input("Введите количество элементов первого набора чисел: ")))
list_2 = generator(int(input("Введите количество элементов второго набора чисел: ")))
print(f"Первый набор чисел: {list_1}")
print(f"Второй набор чисел: {list_2}")
repeats = compare_lists(list_1,list_2)
print(f"Повторяющиеся элементы из двух списков: {repeats}")




