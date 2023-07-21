# print("Это Конъюнкция ∧")
# print(True and False)
# print(True and True)
# print(False and True)
# print(False and False)

# print("Это Дизъюнкция ∨")
# print(True or False)
# print(True or True)
# print(False or True)
# print(False or False)
from random import *
x = choice([True,False])
y = choice([True,False])
z = choice([True,False])

def predicate_generator(predicate_count):
    predicates = []
    for i in range(predicate_count):
        predicates.append(choice([True,False]))
    return predicates



def de_morgan(predicates):
    return not(predicates[0] or predicates[1] or predicates[2]) == (not(predicates[0]) and not(predicates[1]) and not(predicates[2]))
        
        
count_predicate = 3
j = 0
while(j < 100):
    print(de_morgan(predicate_generator(count_predicate)))
    j += 1