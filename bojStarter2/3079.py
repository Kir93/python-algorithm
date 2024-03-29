from sys import stdin

n, m = map(int, stdin.readline().split())
ls = [int(stdin.readline()) for _ in range(n)]

l, r = min(ls), max(ls) * m
ans = r

while l <= r:
    total = 0
    mid = (l + r) // 2

    for i in range(n):
        total += mid // ls[i]

    if total >= m:
        r = mid -1
        ans = min(mid, ans)

    else:
        l = mid + 1

print(ans)