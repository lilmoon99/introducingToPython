# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.

# Пример:
# n = 6 -> (1, 4, 1)  
# n = 24 -> (4, 16, 4)   
# n = 60 -> (10, 40, 10)
n = 120
m = int(n / 6)
peter = m
sergey = m
kate = 4 * m
print(peter,kate,sergey)