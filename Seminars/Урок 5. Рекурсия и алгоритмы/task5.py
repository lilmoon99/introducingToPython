
count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york, count_chicago ]
count_all = [count_angola, count_usa]
print(count_all)


def count(elements):
    if type(elements) == int:
        return elements

    summa = 0
    for element in elements:
        summa += count(element)
    return summa

print(count(count_all))