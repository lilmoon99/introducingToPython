# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# A = int(input("Enter a number: "))
# i = 2
# febonachi = []
# febonachi.append(0)
# febonachi.append(1)
# while febonachi[i-1] < A:
#     febonachi.append(febonachi[i - 1] + febonachi[i - 2])
#     i += 1
# iter = 0
# while len(febonachi) > iter:
#     if febonachi[iter] == A:
#         print(iter)
#     else:
#         print("-1")
#     iter += 1
# print(f"{A} не является числом фибаначи")
# print(i)
# print(febonachi)

# a = int(input('Enter number: '))
# n1 = 0  # первое число
# n2 = 1  # второе число
# n3 = 0  # сумма двух предыдущих членов

# i = 1
# while n1 < a:
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     i += 1
#     if n1 > a:
#         i = -1
# print(i)

A = int(input("Введите проверяемое число"))
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711

current = 1 #текущее
previous = 0 #предыдущее

i = 2 #
while current < A:
    temporary = current
    current = previous + current
    previous = temporary
    i = i + 1
#print(current)
if current == A:
    print(i)
else: 
    print(-1)

