ls = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for row in range(x, x + 10):
        for col in range(y, y + 10):
            ls[row][col] = 1

r = 0
for row in ls: r += row.count(1)
print(r)