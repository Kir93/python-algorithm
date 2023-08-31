for _ in range(int(input())):
    button = False
    ls = list(map(int, input()))
    r = ''
    for i in range(len(ls) - 1, -1, -1):
        if ls[i] <= ls[i - 1]: continue
        else:
            ls[i:] = sorted(ls[i:])
            for idx, n in enumerate(ls[i:]):
                if ls[i - 1] < n:
                    ls[i - 1], ls[idx + i] = ls[idx + i], ls[i - 1]
                    button = True
                    for j in range(len(ls)):
                        r += str(ls[j])
                    print(r)
                    break
            if button: break
    if not button: print('BIGGEST')