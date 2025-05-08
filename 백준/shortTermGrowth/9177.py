import sys
input = sys.stdin.readline
from collections import deque

def bfs(words):
    A, B, C = words
    dq = deque([(len(A), len(B), len(C))])
    visited = [[0] * (len(B)+1) for _ in range(len(A)+1)]
    while dq:
        ai, bi, ci = dq.popleft()
        if ai == bi == ci == 0:
            return True
        elif ci == 0:
            return False

        if ai > 0 and A[ai-1] == C[ci-1] and visited[ai-1][bi] == 0:
            visited[ai-1][bi] = 1
            dq.append([ai-1, bi, ci-1])
        if bi > 0 and B[bi-1] == C[ci-1] and visited[ai][bi-1] == 0:
            visited[ai][bi-1] = 1
            dq.append([ai, bi-1, ci-1])
    else:
        return False

n = int(input())
for i in range(n):
    words = list(map(str, input().split()))
    if bfs(words):
        print("Data set %d: yes" %(i+1))
    else:
        print("Data set %d: no" %(i+1))