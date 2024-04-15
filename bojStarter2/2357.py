import math
import sys

input = lambda: sys.stdin.readline().rstrip()

def make_seg(idx, s, e):

    if s == e:
        seg[idx] = (arr[s], arr[s])
        return seg[idx]

    mid = (s + e) // 2

    l = make_seg(idx * 2, s, mid)
    r = make_seg(idx * 2 + 1, mid + 1, e)

    seg[idx] = (min(l[0], r[0]), max(l[1], r[1]))
    return seg[idx]


def f(s, e, idx):

    if e < a or b < s:
        return (1000000000, 0)

    mid = (s + e) // 2

    if a <= s and e <= b:
        return seg[idx]

    else:
        l = f(s, mid, idx * 2)
        r = f(mid + 1, e, idx * 2 + 1)
        return (min(l[0], r[0]), max(l[1], r[1]))


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

b = math.ceil(math.log2(n)) + 1
node_n = 1 << b
seg = [0 for _ in range(node_n)]
make_seg(1, 0, len(arr) - 1)

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    ans = f(0, len(arr) - 1, 1)
    print(ans[0], ans[1])