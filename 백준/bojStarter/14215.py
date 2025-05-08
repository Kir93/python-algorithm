ls = sorted(list(map(int, input().split())))

if ls[0] + ls[1] > ls[2]: print(sum(ls))
else: print((ls[0] + ls[1]) * 2 - 1)