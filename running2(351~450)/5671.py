while True:
    try:
        n, m = map(int, input().split())
    except: break
    c = 0
    for i in range(n, m+1):
        r = set()
        n = str(i)
        for char in n: r.add(char)
        if len(n) == len(r): c += 1
    print(c)