ls = [int(input()) for _ in range(6)]
print(sum(ls) - min(ls[:4]) - min(ls[4:]))