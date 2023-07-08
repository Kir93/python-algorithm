n = int(input())
i = 1
r = 0
while n > 0:
    if i > n: i = 1
    n -= i
    i += 1
    r += 1
print(r)