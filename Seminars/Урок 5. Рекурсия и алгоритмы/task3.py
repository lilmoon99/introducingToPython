# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def simple_number(N,divider = 2):
    if N == divider:
        return True
    elif N % divider == 0: return False
    else: return simple_number(N,divider + 1)
    # return simple_number(N,divider + 1)

print(simple_number(4))

