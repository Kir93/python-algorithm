c = [list(map(int,input().split())) for _ in range(5)]
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

def check():
    bingo = 0

    for x in c:
        if x.count(0) == 5: bingo += 1

    for i in range(5):
        y = 0
        for j in range(5):
            if c[j][i] == 0: y += 1
        if y == 5: bingo += 1

    d1 = 0
    for i in range(5):
        if c[i][i] == 0: d1 += 1
    if d1 == 5: bingo += 1

    d2 = 0
    for i in range(5):
        if c[i][4-i] == 0: d2 += 1
    if d2 == 5: bingo += 1

    return bingo

cnt = 0
for i in range(25):
    for j in range(5):
        for k in range(5):
            if mc[i] == c[j][k]:
                c[j][k] = 0
                cnt += 1

    if cnt >= 12:
        result = check()
        if result >= 3:
            print(i + 1)
            break