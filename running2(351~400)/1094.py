x = int(input())
ls = [64, 32, 16, 8, 4, 2, 1]
c = 0

for i in range(len(ls)):
    if x >= ls[i]:
        c += 1
        x -= ls[i]
    if x == 0: break

print(c)