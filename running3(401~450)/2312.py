for _ in range(int(input())):
    n = int(input())
    ls = []
    x = 2
    while x <= n:
        if n%x == 0:
            n //= x
            ls.append(x)
        else: x += 1
    ls.sort()
    sls = set(ls)
    r = sorted(list(sls))

    for i in range(len(r)): print(r[i], ls.count(r[i]))