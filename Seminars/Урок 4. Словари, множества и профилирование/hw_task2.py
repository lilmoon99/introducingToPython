# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — 
# на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым 
# кустом заданной во входном списке урожайности грядки.
from random import *
def generate_bush(bushes_count:int) -> list:
    temp_list = []
    for i in range(bushes_count):
        temp_list.append(randint(1,5))
    return temp_list

def collect_berries(bushes_list:list) -> list:
    temp_collected_berries = []
    max_berries_count = 0
    for i in range(len(bushes_list)):
        if max_berries_count < bushes_list[i - 1] + bushes_list[i] + bushes_list[i - len(bushes_list) + 1]:
            max_berries_count = bushes_list[i - 1] + bushes_list[i] + bushes_list[i - len(bushes_list) + 1]
        temp_collected_berries.append(bushes_list[i - 1] + bushes_list[i] + bushes_list[i - len(bushes_list) + 1])
    return temp_collected_berries

def max_berries_index(collected_berries_list:list) -> list:
    max_berries_index_list = []
    max_berries = max(collected_berries_from_bushes)
    for i in range(len(collected_berries_list)):
        if max_berries == collected_berries_list[i]:
            max_berries_index_list.append(i)
    return max_berries_index_list

def max_berries_index_human_version(index_list:list) -> list:
    temp_list = []
    for i in range(len(index_list)):
        temp_list.append(index_list[i]+1)
    return temp_list

bushes_count = int(input("Введите количество кустов: ")) # Ввод количества кустов с клавиатуры
bushes = generate_bush(bushes_count) # генерация ягод на кустах
collected_berries_from_bushes = collect_berries(bushes) # Количество ягод, которые может собрать коллектор
max_berries_index_list = max_berries_index(collected_berries_from_bushes) # Индексы, на которых находятся максимальное количество ягод
max_berries_index_list_human_version = max_berries_index_human_version(max_berries_index_list) # Индексы с максимальным количеством ягод с удобным для человека отображением
print(f"Количество ягод на кустах: {bushes}")
print(f"Количество ягод, которые может собрать коллектор: {collected_berries_from_bushes}")
print(f"Максимальное количество ягод можно собрать с куста(-ов) №: {str(max_berries_index_list_human_version).replace('[',' ').replace(']','')}")