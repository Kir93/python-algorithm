for _ in range(int(input())):
    n, d = map(int, input().split())
    r = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        if v * (f/c) >= d: r += 1
    print(r)