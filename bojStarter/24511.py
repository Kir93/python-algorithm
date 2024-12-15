import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

m = int(input())
list_c = list(map(int, input().split()))

res = deque()

for qs in range(n):
    if list_a[qs] == 0: res.appendleft(list_b[qs])
        
for i in range(m):
    res.append(list_c[i])
    print(res.popleft(), end=' ')