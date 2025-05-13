import sys
input = sys.stdin.readline

def update(idx, val):
    idx += 500001
    if tree[idx] < val:
        tree[idx] = val
        while idx > 1:
            tree[idx // 2] = max(tree[idx], tree[idx ^ 1])
            idx >>= 1

def query(left, right):
    left += 500001
    right += 500001
    ret = 0
    while left < right:
        if left % 2 == 1:
            ret = max(ret, tree[left])
            left += 1
        
        if right % 2 == 1:
            ret = max(ret, tree[right - 1])
        
        left >>= 1
        right >>= 1
    return ret

N, k, d = map(int, input().split())
S = [0] + [*map(int, input().split())]
tree = [0 for _ in range(10 ** 6 + 2)]

dp = [0 for _ in range(N + 1)]
mod_val = [0 for _ in range(k)]

for a in range(1, N + 1):
    i = S[a]
    dp[a] = max(mod_val[i % k], query(max(1, i - d), min(500000, i + d) + 1)) + 1
    if tree[500001 + i] < dp[a]:
        update(i, dp[a])
    mod_val[i % k] = max(mod_val[i % k], dp[a])
    
print(max(dp))