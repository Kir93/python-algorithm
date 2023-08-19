while True:
    x = input()
    if x == '*': break
    rx = x.split()
    r = rx[0][0].lower()
    for y in rx:
        if r != y[0].lower():
            print('N')
            r = ''
            break
    if r != '': print('Y')