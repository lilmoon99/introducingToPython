from decimal import *
a = 451.9421
def numbers_after_dot_converter(number):
    numbers_after_dot = (Decimal (str(number)).as_tuple().exponent*(-1))
    while numbers_after_dot > 0:
        number *= 10
        numbers_after_dot -= 1
    return round(number)

def sum_calculator(number):
    summary = 0
    while number > 0:
        temp = number % 10
        summary += temp
        number = number // 10
    return summary
    
after_convert = numbers_after_dot_converter(a)
summary = sum_calculator(after_convert)
print(summary)


