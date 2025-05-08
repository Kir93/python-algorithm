while True:
    ls = list(map(int, input().split()))
    if ls[0] == 0: break
    ls = ls[1:]
    r = []
    for i in range(len(ls)):
        if i == 0: r.append(ls[i])
        elif r[-1] != ls[i]: r.append(ls[i])
    print(*r, '$')