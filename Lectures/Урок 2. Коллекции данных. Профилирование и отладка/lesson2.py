# list_1 = []
# list_1 = list()
# list_1 = [1,2,3,8]

# # print(list_1)
# # print(*list_1)

# # for i in list_1:
# #     print(i)
    
# # print(len(list_1))
# print(list_1[0]) #1
# print(list_1[-1]) #8


# list_2 = [1,5]
# print(list_2)
# list_2.append(8)
# print(list_2)
# list_2.append(85)

# list_3 = []
# for i in range(5):
#     list_3.append(i)
#     print(list_3)
    
# list_3 = [12, 7, -1, 21, 0]
# print(list_3.pop()) # 0
# print(list_3) # [12, 7, -1, 21]
# print(list_3.pop()) # 21
# print(list_3) # [12, 7, -1]
# print(list_3.pop()) # -1
# print(list_3) # [12, 7]

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменятькортеж)

# dictionary = {}
# dictionary = dict()
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# # print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# dictionary[895] = 123
# print(dictionary)

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# list_1 = [exp for item in iterable]

# list_1 = [exp for item in iterable (if conditional)]

# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]
