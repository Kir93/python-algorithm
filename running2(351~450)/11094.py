for _ in range(int(input())):
    x = input().split('Simon says')
    if len(x) > 1: print(*x[1:])