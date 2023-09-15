for _ in range(int(input())):
    n = int(input())
    r = 0
    for i in range(1, n+1): r += i*sum([j for j in range(1, i+2)])
    print(r)