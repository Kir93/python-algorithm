while True:
    ls = list(map(int, input().split()))

    if ls[0] == 0:
        break
    n = 1

    for i in range(ls[0]):
        sf = ls[2*i + 1]
        p = ls[2*i + 2]
        n = n*sf - p

    print(n)