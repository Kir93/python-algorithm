a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

r = 0
ice = bool(a < 0)

while a != b:
    if a < 0:
        a += 1
        r += c
    elif a == 0 and ice:
        r += d
        ice = False
    else:
        r += e
        a += 1
else:
    print(r)