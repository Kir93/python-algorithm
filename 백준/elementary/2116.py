N = int(input())

dice = []
for _ in range(N): dice.append(list(map(int, input().split())))
rotate = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}

maxnum = 0

for i in range(6):
    result = []
    temp = [1, 2, 3, 4, 5, 6]
    temp.remove(dice[0][i])
    next = dice[0][rotate[i]]
    temp.remove(next)
    result.append(max(temp))

    for j in range(1, N):
        temp = [1, 2, 3, 4, 5, 6]
        temp.remove(next)
        next = dice[j][rotate[dice[j].index(next)]]
        temp.remove(next)
        result.append(max(temp))
        
    result = sum(result)

    if maxnum < result: maxnum = result

print(maxnum)