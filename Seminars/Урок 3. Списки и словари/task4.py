# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

sp = []
length = int(input("Enter an array length: "))
for i in range(length):
    sp.append(int(input(f"Введите {i+1} элемент: ")))
print(sp)
counts = 0
for i in range(len(sp) - 1):
    k = i + 1
    if sp[k] > sp[i]:
        counts += 1
        print(f"{sp[i]} < {sp[k]}")
        
print(f"Количество элементов массива, больших предыдущего (элемента с предыдущим номером): {counts}")