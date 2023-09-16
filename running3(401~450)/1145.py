ls = sorted(list(map(int, input().split())))
for i in range(ls[-3], 1000000001):
    s = 0
    for x in ls:
        if i%x == 0: s += 1
    if s >= 3:
        print(i)
        break