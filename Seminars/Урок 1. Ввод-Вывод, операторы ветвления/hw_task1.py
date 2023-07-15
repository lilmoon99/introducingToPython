# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

n = 552
def sum_of_numbers(n):
    list = 0
    while n > 0:
        list = list + n % 10
        n = n // 10
    return list
print(sum_of_numbers(n))