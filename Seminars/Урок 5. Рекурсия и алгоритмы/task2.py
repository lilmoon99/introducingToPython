# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change_marks(list,index):
    if index == len(list):
        return list
    if list[index] == max(list):
        list[index] = 1
    return change_marks(list,index + 1)
sp = [4, 3, 3, 3, 4]
print(change_marks(sp,0))