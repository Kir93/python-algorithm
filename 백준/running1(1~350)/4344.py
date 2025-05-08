for _ in range(int(input())):
    ls = list(map(int, input().split()))
    n = ls.pop(0)
    d = sum(ls) // n
    r = 0
    for x in ls:
        if d < x: r += 1
    print(f'{(r/n)*100:.3f}%')