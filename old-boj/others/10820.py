while True:
    try:
        r = [0 for _ in range(4)]
        s = list(input())
        for x in s:
            if x.islower(): r[0] += 1
            elif x.isupper(): r[1] += 1
            elif x.isdigit(): r[2] += 1
            elif x.isspace(): r[3] += 1
        for y in r: print(y, end=' ')
    except EOFError:
        break
