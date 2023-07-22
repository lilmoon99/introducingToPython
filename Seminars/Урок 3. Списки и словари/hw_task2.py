# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.



def closer_element(list,number_to_find):
    dif_min = number_to_find - list_1[0]
    temp_dif = 0
    index = 0
    for i in range(len(list)):
        temp_dif = number_to_find - list_1[i]
        if number_to_find == list[i]:
            index = i
            break
        if temp_dif > 0:
            if dif_min >= temp_dif:
                index = i
                dif_min = temp_dif
        else:
            temp_dif = temp_dif * (-1)
            if dif_min >= temp_dif:
                index = i
                dif_min = temp_dif

    return list[index]
        
        
list_1 = [1, 12, 6, 7, 8, 15]
k = 11
print(closer_element(list_1,k))