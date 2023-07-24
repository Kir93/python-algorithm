n, T = map(int, input().split())
ls = list(map(int, input().split()))
r = 0
while T >= 0 and len(ls) > 0:
    if T - ls[0] >= 0:
        r += 1
        T -= ls[0]
        ls.pop(0)
    elif T - ls[0] < 0: break
print(r)