Y = [30, 10]
M = [60, 15]

int(input())
ls = list(map(int, input().split()))
y = 0
m = 0

for x in ls:
    y += x//Y[0] * Y[1] + Y[1]
    m += x//M[0] * M[1] + M[1]

if y < m: print("Y", y)
elif y > m: print("M", m)
else: print("Y M", y)