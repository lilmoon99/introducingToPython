# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1, ..., an, ..., где
# a0 = 0, 
# a1 = 1, 
# ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fib(N):
    if N == 0:
        return N
    elif N == 1:
        return N
    else:
        return fib(N-1) + fib(N - 2)
    
print(fib(7))