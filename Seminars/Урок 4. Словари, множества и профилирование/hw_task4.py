import re
# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re



# s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
# result = re.match('DC',s)
# result = re.search('DC',s)
# result = re.findall('DC',s)
# result = re.split('/',s,maxsplit= 3)
# result = re.sub('A','D',s)
# result = re.fullmatch('A',s)
# print(result)

# s = "098123asd+ asdasd       --------- jaksdhb ba^7 JAKSHDJKABKkajsdhakjASD"

# result = re.search(r"j.k",s)
# result = re.search(r"\d\d",s)
# result = re.search(r"\D",s)
# result = re.search(r"\s",s)
# result = re.search(r"\S",s)
# result = re.search(r"\w",s)
# result = re.search(r"\W",s)
# result = re.search(r"\bJAK",s)
# result = re.search(r"\d*",s)
# result = re.search(r"[ghkjd]",s)
# result = re.search(r"[^4-6]",s)
# result = re.search(r"[H|f]",s)
# result = re.search(r"\d{1,3}",s)
# result = re.search(r"\d{,4}",s)
# s = "Привет! Как дела? А у меня нормально"
# result = re.findall(r"[бвгджзйклмнпрстфхчцшщБВГДЙЖЗКЛМНПРСТФХЦШЩ]\w+",s)
# print(result)

string1 = "2x^2 + 4x + 5 = 0"
string2 = "5x^3 - 3x^2 - 12 = 0"

result1 = re.split(r'[/+--//=*/]',string1)
result2 = re.split(r'[/+--//=*/]',string2)
print(result1)
print(result2)
operands1 = re.findall(r"[+-/=/]",string1)
operands2 = re.findall(r"[+-/=/]",string2)
print(operands1)
print(operands2)