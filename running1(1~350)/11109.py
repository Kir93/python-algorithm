for _ in range(int(input())):
    d, n, s, p = map(int, input().split())
    r = (s - p) * n - d
    if r > 0: print('parallelize')
    elif r == 0: print('does not matter')
    else: print('do not parallelize')