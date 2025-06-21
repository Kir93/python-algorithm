n, m, l = map(int, input().split())
r = -1

ls = [0] * n
pick = 0

while True:
    if max(ls) >= m: break
    ls[pick] += 1
    r += 1

    if ls[pick]//2 == 0:    
        if pick + l < n:
            pick += l
        else:
            pick = pick + l - n
    else:
        if pick - l >= 0:
            pick -= l
        else:
            pick = n + (pick - l)

print(r)