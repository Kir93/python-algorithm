r = 0
m = [int(input()) for _ in range(10)]
for x in m:
    r += x
    if r >= 100:
        if r - 100 > 100 - (r - x): r -= x
        break
print(r)