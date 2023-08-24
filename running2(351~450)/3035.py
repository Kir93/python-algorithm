r, c, zr, zc = map(int, input().split())
ls = []
res = ''
for _ in range(r):
    old = input()
    for i in range(zr):
        for j in range(c):
            res += old[j] * zc
        ls.append(res)
        res = ''
for x in ls: print(x)