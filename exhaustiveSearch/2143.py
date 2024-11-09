import bisect
import sys

T = int(sys.stdin.readline())
a = int(sys.stdin.readline())
an = list(map(int, sys.stdin.readline().split()))

b = int(sys.stdin.readline())
bn = list(map(int, sys.stdin.readline().split()))

aan, bbn = [], []

for i in range(a):
    for j in range(i+1, a+1):
        aan.append(sum(an[i:j]))

for i in range(b):
    for j in range(i + 1, b + 1):
        bbn.append(sum(bn[i:j]))

aan.sort()
bbn.sort()

ans = 0

for i in range(len(aan)):
    bmp = T - aan[i]
    left = bisect.bisect_left(bbn, bmp)
    right = bisect.bisect_right(bbn, bmp)
    ans += (right - left)

print(ans)