ls = list(map(int, input().split()))
while True:
    for i in range(len(ls)-1):
        if ls[i] > ls[i+1]:
            ls[i], ls[i+1] = ls[i+1], ls[i]
            print(*ls)

    if ls == [1, 2, 3, 4, 5]: break