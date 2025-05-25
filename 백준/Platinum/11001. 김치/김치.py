n, d = map(int, input().split())

t = list(map(int, input().split()))
v = list(map(int, input().split()))

dp = [0 for _ in range(n)]


def dnc(start, end, left, right):
    if start > end:
        return
    mid = start + end >> 1
    opt = left
    for j in range(left, min(right + 1, mid + d + 1)):
        if v[mid] + (j - mid) * t[j] > v[mid] + (opt - mid) * t[opt]:
            opt = j
    dp[mid] = v[mid] + (opt - mid) * t[opt]
    dnc(start, mid - 1, left, opt)
    dnc(mid + 1, end, opt, right)


dnc(0, n - 1, 0, n - 1)

print(max(dp))