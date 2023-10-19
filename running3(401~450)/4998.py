while True:
    try:
        n, m, b = map(float, input().split())
        c = 0
        while b > n:
            n += n * m / 100
            c += 1
        print(c)
    except: break