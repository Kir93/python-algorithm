while True:
    n = int(input())
    if n == 0: break
    while True:
        if n < 10:
            print(n)
            break
        print(n, end=' ')
        ls = list(str(n))
        n = 1
        for i in range(len(ls)): n *= int(ls[i])