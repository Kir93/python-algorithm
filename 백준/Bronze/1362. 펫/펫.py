i = 0
while True:
    death = 0
    i += 1
    o, w = map(int, input().split())
    if o == w == 0:
        break
    while True:
        e, n = map(str, input().split())
        if e == '#' and n == '0':
            break
        if e == 'F':
            w += int(n)
        elif e == 'E':
            w -= int(n)
        
        if w <= 0:
            death = 1
    if death == 1:
        print(f'{i} RIP')
    else:
        if o/2 < w < o*2:
            print(f'{i} :-)')
        else:
            print(f'{i} :-(')
        