import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())
dq = list(i for i in range(1, n+1))
dq = deque(dq)
while dq:
    for _ in range(k-1):
        dq.append(dq.popleft())
    dq.popleft()
    if len(dq) == 1:
        print(dq.pop())
