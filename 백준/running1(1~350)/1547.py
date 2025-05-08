ls = [1, 0, 0]
for _ in range(int(input())):
    x, y = map(int, input().split())
    ls[x-1], ls[y-1] = ls[y-1], ls[x-1]
print(ls.index(1) + 1)