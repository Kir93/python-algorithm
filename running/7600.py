while True:
    w = set(input().lower().rstrip())
    r = 0
    if w == {'#'}: break
    for x in w:
        if ord(x) >= 97 and ord(x) <= 122: r += 1
    print(r)