# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
import math
def Drive():
    n = 700
    m = 750

    speed = n / 24
    print(speed)
    time = int(m / speed)
    print(time)
    time_days = math.ceil(time/24)
    print(time_days)

Drive()