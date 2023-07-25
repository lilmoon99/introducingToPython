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
# x = choice([True,False])
# y = choice([True,False])
# z = choice([True,False])

def predicate_generator(predicate_count):
    predicates = []
    for i in range(predicate_count):
        predicates.append(choice([True,False]))
    return predicates



def de_morgan(predicates):
    left_side = predicates[0]
    right_side = not predicates[0]
    for i in range(1,len(predicates)):
        left_side = left_side or predicates[i]
        right_side = right_side and not predicates[i]
    return not left_side == right_side       
        

j = 0
while(j < 100):
    count_predicate = randint(3,15)
    print(de_morgan(predicate_generator(count_predicate)))
    j += 1