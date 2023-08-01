from random import *

def square(sp):
    result = []
    for item in sp:
        result.append(item**2)
    return result

def find4_and_square(sp):
    
    result = []
    for item in sp:
        if item > 4:
            result.append(item**2)
    return result
    
sp = [1, 5, 3, 8, 10, 2]
# print(sum(sp))
# print(max(sp))
square(sp)
print(5 in sp)
print(5 not in sp)
print([item**2 for item in sp])
print(find4_and_square(sp))
print([item ** 2 for item in sp if item > 4])
print([randint(0,10) for _ in range(10)])