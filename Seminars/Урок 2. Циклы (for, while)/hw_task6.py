# Валентина прогуляла лекцию по математике.
# Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

# Решить такое вручную, как вы понимаете, практически нереально.
# Вот Валентина и обратилась к вам за помощью.
# Помогите ей (при помощи функции all_divisors(number), которую напишете сами).
# Постарайтесь найти самое оптимальное решение.
# Результат представьте в виде списка (не забудьте отсортировать по возрастанию).
number = 23436
def all_divisors(number):
    temp_number = number
    simple_mults = []
    simple_dividers = [] #Простые множители. Умножение даст число number
    while temp_number > 1:
        divider = 2
        while temp_number // divider:
            if temp_number % divider == 0:
                simple_mults.append(temp_number//divider)
                temp_number = temp_number // divider
                simple_dividers.append(divider)
            else:
                divider += 1
                continue
    simple_mults.reverse()
    simple_mults.append(number)
    return simple_mults

print(f"Делители числа {number}: {str(all_divisors(number)).replace('[','').replace(']','')}")
