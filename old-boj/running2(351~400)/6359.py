for _ in range(int(input())):
    n = int(input())
    ls = [True] * (n + 1)
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            if ls[j] == True: ls[j] = False
            else: ls[j] = True
    print(ls[1:].count(True))