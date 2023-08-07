# def create_phrase(func,word):
#     print(func(word))
    
# def hello(s):
#     return f"Hello, {s}"

# def bye(s):
#     return f"{s} bye - bye"
# create_phrase(hello,'world')
# create_phrase(bye,"world")
# create_phrase(hello,'Aynur')
# create_phrase(bye,"Aynur")

# def calc_power(degree):
#     def power(number):
#         return number ** degree
#     return power

# # print(calc_power(3)(4))

# square = calc_power(2)
# cube = calc_power(3)

# print(square(8))
# print(cube(3))

# print((lambda x , y: x + y)(5,8))

# calc = {"+": lambda x, y : x + y,
#         "-": lambda x, y : x - y,
#         "*": lambda x, y : x * y,
#         "/": lambda x, y : x / y
# }

# print(calc["*"](5,300))
# names = ["Петя","Ваня","Саша"]
# sp = [5,8,1,11,3,2]

# print(*map(lambda item: item **2,sp))
# print(list(map(lambda item: item **2,sp)))
# print(*map(lambda item: item **2 if item > 5 else 0,sp))
# print(*filter(lambda item: item > 5,sp))
# for i, v in enumerate(sp):
#     print(i,v)
    
# for x1, x2 in zip(names,sp):
#     print(x1,x2)