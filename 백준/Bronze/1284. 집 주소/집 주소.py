while True:
    n = input()
    r = 0

    if n == "0": break

    r += 2
    for x in n:
        if x == '1': r += 2
        elif x == '0': r += 4
        else: r += 3
        r += 1

    print(r - 1)