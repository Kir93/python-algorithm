import sys
from collections import deque
input = sys.stdin.readline

ans = []
n = int(input())
q = deque(enumerate(map(int, input().split())))

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0: q.rotate(-(paper - 1))
    elif paper < 0: q.rotate(-paper)

print(' '.join(map(str, ans)))