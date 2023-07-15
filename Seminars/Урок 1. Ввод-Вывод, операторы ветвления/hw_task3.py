# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
# Пример:
# n = 385916 -> yes
# n = 123456 -> no
n = 123456
def lucky_ticket(ticket_number):
    first_part = 0
    second_part = 0
    while ticket_number > 0:
        temp = ticket_number % 10
        if ticket_number > 999:
            first_part = first_part + temp
        else:
            second_part = second_part + temp
        ticket_number = ticket_number // 10
    if(first_part == second_part):
        return "yes"
    else: 
        return "no"
print(lucky_ticket(n))