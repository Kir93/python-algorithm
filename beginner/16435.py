N , L = map(int,input().split())

h = list(map(int,input().split()))
h.sort()
for _ in h:
    if _ <= L:
        L += 1
print(L)