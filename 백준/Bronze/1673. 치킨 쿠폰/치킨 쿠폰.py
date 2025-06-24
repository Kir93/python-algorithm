while True:
    try:
        n, k = map(int, input().split())
        r = 0
        r += n
        while n // k:
            r += n // k
            n = n // k + n % k
        print(r)
    except:
        break