def Summ(N):
    summa = 0
    while True:
        summa = summa + N
        N = N - 1
        if N == 0:
            break
    return summa

def Summ_rec(N):
    if N == 1:
        return 1
    return N + Summ_rec(N-1)

print(Summ_rec(4))