def sum(a, b):
    if b == 0:
        if a == 0:
            return 0
        return sum(a-1,b) + 1
    return sum(a,b-1) + 1
a = 5
b = 54
print(f"{a} + {b} = {sum(a,b)}")