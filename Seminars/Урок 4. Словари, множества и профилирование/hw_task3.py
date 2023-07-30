# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции

def convert_to(number_to_convert:int,base:int) -> list:
    converted_number_list = []
    while(number_to_convert >= base):
        converted_number_list.append(number_to_convert % base)
        number_to_convert = number_to_convert // base
        if number_to_convert < base:
            converted_number_list.append(number_to_convert)
    converted_number_list.reverse()
    return converted_number_list

x = int(input("Enter a number to convert: "))
base = int(input("Enter a base: 2 or 8? "))
if base == 2:
    x_n = f'{x:b}'
else:
    x_n = f'{x:o}'
print(f"Converted by built-in function: {x_n}")
converted = convert_to(x,base)
converted_str = ''.join(str(element) for element in converted)
print(f"Converted by self-made function: {converted_str}")

print(f"Is correct: {x_n == converted_str}")