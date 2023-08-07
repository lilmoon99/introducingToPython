# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:
values = [0, 2, 10, 6]
values1 = [1,3,5,7,9,11]

def same_by(characteristic, objects):
    if len(objects) == 0:
      return True
    temp = list(map(characteristic,objects))
    return max(temp) == min(temp)

if same_by(lambda x: x % 2, values):
  print('same')
else:
  print('different')
