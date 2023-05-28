n, m = map(int, input().split())
ls = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    temp = ls[i-1:j]
    temp.reverse()
    ls[i-1:j] = temp
print(*ls)