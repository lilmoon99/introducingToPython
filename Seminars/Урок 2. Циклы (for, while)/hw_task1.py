# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
from random import choice
def coin_init(coins_number):
    coins_list = []
    for i in range(coins_number):
        coins_list.append(choice(["Орёл" , "Решка"]))
    return coins_list

def print_list(list):
    for i in list:
        print(i)
        
def flip(list):
    heads = 0
    tails = 0
    for i in list:
        if i == "Решка":
            tails += 1
        else:
            heads += 1
    if heads == 0 or tails == 0:
        print("Ничего не нужно делать!")
    elif heads < tails:
        print(f"Нужно перевернуть {heads} орла(-ов)!")
    elif heads > tails:
        print(f"Нужно перевернуть {tails} решек(-и)!")
    else:
        print("Орёл = Решка")
        

n = int(input("Enter a coins number: "))
coins = coin_init(n)
print_list(coins)
flip(coins)

