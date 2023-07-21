# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

sp = [1,1,2,0,-1,3,4,4]
# counts = 0

# while len(sp) > 0:
#     pop =  sp.pop()
#     if pop == sp[]:
#         counts += 1
# print(counts)
dif_numbers = []
for number in sp:
    if number not in dif_numbers:
        dif_numbers.append(number)
        
print(len(dif_numbers))

s = set(sp)
print(len(s))