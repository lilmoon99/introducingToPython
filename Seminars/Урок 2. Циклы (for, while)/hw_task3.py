# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import math

N = int(input("Введите число N: "))
base = 2

def calculate(N):
    list = []
    for i in range(N):
        list.append(pow(base,i))
    return list
        
def print_list(list):
    print(f"Степени числа {base} до ^{N}")
    for i in list:
        print(i)
        
        
pow2 = calculate(N)
print_list(pow2)