ls = []

for _ in range(int(input())):
    ls.append(list(map(int, input().split())))

ls.sort(key=lambda x: -x[2])

print(*ls[0][:2])
print(*ls[1][:2])

i = 2

if ls[0][0] == ls[1][0]:
    while ls[0][0] == ls[i][0]:
        i += 1

print(*ls[i][:2])