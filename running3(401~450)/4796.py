i = 0
while True:
    i += 1
    l, p, v = map(int, input().split())
    if l == p == v == 0: break
    a = v//p
    b = v%p
    if l<b: b = l
    print(f'Case {i}: {a*l+b}')