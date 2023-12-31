# Необходимо написать программу для автоматического перевода различных валютных счетов в рублевые.
# Начальные данные программы это три различных списка - Фамилии владельцев банковских счетов, указание валют счетов, соответствующее состояние счетов. То есть у Иголкина счет в евро и там лежит 50000, и так далее.
# Также вначале заданы отношения курса рубля к доллару и евро.

surnames = ["Иванов", "Карпов", "Иголкин"]
currency_name = ["рубль", "доллар", "евро"]
balances = [30000, 40000, 50000]
dollar = 90
euro = 99

# Вам необходимо написать функцию calc, которая на входе принимает только один аргумент, далее надо применить ее в комбинациях с map и zip.

#   На выходе программы должны быть три пары значений - фамилии владельцев счетов и состояние рублевого счета.

def calc(currency,balance):
    result = balance
    if currency == "доллар":
        result *= dollar
    elif currency == "евро":
        result *= euro
    return result
new_balances = list(map(calc,currency_name,balances))
print(new_balances)
print(*zip(surnames,new_balances))