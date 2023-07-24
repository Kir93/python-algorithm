n = input()
ls = [1, 0, 0]
for x in n:
    if x == 'A': ls[0], ls[1] = ls[1], ls[0]
    elif x == 'B': ls[1], ls[2] = ls[2], ls[1]
    elif x == 'C': ls[0], ls[2] = ls[2], ls[0]
print(ls.index(1) + 1)