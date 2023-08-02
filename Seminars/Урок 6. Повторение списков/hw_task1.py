# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a0 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression():
    first = int(input("Enter a first element: "))
    diff = int(input("Enter a difference: "))
    length = int(input("Enter a length: "))
    index = 1
    temp_list = []
    while index <= length:
        temp_list.append(first + (index - 1)* diff)
        index += 1
    return temp_list

print(arithmetic_progression())