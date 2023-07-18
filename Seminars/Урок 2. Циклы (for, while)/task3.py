# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
import random
import math
watermelon_count = int(input("Enter a watermelons number: "))
watermelon_weight = []
for i in range(watermelon_count):
    watermelon_weight.append(round(random.uniform(0.1,10),1))
for i in watermelon_weight:
    print(i)
    
watermelon_weight.sort()

min_weight = watermelon_weight[0]
max_weight = watermelon_weight[len(watermelon_weight) - 1]

print(f"Min wight is {min_weight}")
print(f"Max weight is {max_weight}")
