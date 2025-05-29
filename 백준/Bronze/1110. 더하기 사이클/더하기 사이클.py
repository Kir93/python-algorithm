n = input()
c = '0'
r = 0

if n == '0':
    exit(print(1))

while n != c:
    if len(n) == 1:
        n = '0' + n
    if c == '0':
        c = n
        
    x, y = int(c[1]), int(c[0]) + int(c[1])

    if int(y) >= 10:
        y = str(y)[1]

    c = str(x) + str(y)
    r += 1

print(r)