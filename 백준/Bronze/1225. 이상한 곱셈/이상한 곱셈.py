a, b = map(str, input().split())
r = 0

for x in a:
    for y in b:
        r += int(x) * int(y)

print(r)