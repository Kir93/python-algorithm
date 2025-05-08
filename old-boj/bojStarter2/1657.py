n, m = map(int, input().split())
a = [input() for _ in range(n)]
score = [
    [10, 8, 7, 5, 0, 1],
    [8, 6, 4, 3, 0, 1],
    [7, 4, 3, 2, 0, 1],
    [5, 3, 2, 2, 0, 1],
    [],
    [1, 1, 1, 1, 0, 0]
]

d = [[-1]*(1<<14) for _ in range(14*14)]

def calc(a, b):
    return score[ord(a) - ord('A')][ord(b) - ord('A')]

def dp(idx, state):
    if idx >= n*m: return 0
    if d[idx][state] >= 0: return d[idx][state]
    y, x = divmod(idx, m)
    ans = dp(idx+1, state >> 1)
    if x < m-1 and state & 3 == 0:
        ans = max(ans, dp(idx+2, state >> 2) + calc(a[y][x], a[y][x+1]))
    if y < n-1 and state & 1 == 0:
        ans = max(ans, dp(idx+1, (state >> 1) | (1 << (m-1))) + calc(a[y][x], a[y+1][x]))
    d[idx][state] = ans
    return ans

print(dp(0, 0))