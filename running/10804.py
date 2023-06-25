ls = [i for i in range(1, 21)]
for _ in range(10):
    a, b = map(int, input().split())
    ls[a-1:b] = ls[a-1:b][::-1]
print(*ls)