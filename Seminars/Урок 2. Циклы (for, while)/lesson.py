sp = []
sp.append(65213)
sp.append("privet")
sp.append(4.6)
sp.append([5,7])
sp.append(True)
print(sp)

i = 0
while i < 10:
    print(i, end = " ; ")
    i += 1

for _ in range(4):
    print("hello")
    
for i in sp:
    print(i)
    
for i in range(5,15,3):
    print(i)