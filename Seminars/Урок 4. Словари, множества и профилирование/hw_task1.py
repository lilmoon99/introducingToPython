# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import *
def generator(length:int) -> list:
    temp_list = []
    for i in range(length):
        temp_list.append(randint(1,10))
    return temp_list

def compare_lists(list1:list,list2:list) -> set:
    temp_set = set()
    for i in list1:
        for j in list2:
            if i == j:
                temp_set.add(i)
    temp_set = sorted(temp_set)
    return temp_set

def user_comparator(numbers,set):
    for i in range(numbers):
        if numbers[i] in set:
            print(numbers[i])
list_1 = generator(5)
print(list_1)
list_2 = generator(10)
print(list_2)
repeats = compare_lists(list_1,list_2)
print(repeats)



