# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                     Вывод: 3 3 2 12
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 

def init_list(length:int) -> list:
    temp_list = []
    for i in range(length):
        temp_list.append(int(input(f"Enter {i+1} element: ")))
    return temp_list

def absent_number(list1,list2):
    
    # for i in list1:
    #     if i not in list2:
    #         temp_list.append(i)
            
    temp_list = [item for item in list1 if item not in list2]
    return temp_list

sp1 = init_list(7)
sp2 = init_list(6)

print(absent_number(sp1,sp2))