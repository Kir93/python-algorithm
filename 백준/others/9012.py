for _ in range(int(input())):
    r = 0
    ps = list(input())
    for x in ps:
        if x == '(': r += 1
        elif x == ')': r -= 1
        if r < 0:
            break
    if r == 0: print('YES')
    else: print('NO')