import sys
from collections import deque

A, B, C = map(int, sys.stdin.readline().rstrip().split())

# X+Y 를 X+X + Y-X 로 만들어도 개수에 변함은 없음. 
TOTAL = A+B+C
if TOTAL%3 != 0:
    print(0)
    exit()

visited = [[False]*TOTAL for _ in range(TOTAL)] # [최솟값][최댓값]으로 기록한다. 중간값은 빼면 알 수 있으니까.

q = deque([(A,B)])
visited[A][B] = True
while q:
    a, b = q.popleft()
    c = TOTAL - (a+b)
    if a == b == c:
        print(1)
        exit()
    for X, Y in [(a,b), (a,c), (b,c)]:
        if X == Y:
            continue
        if X > Y:
            X, Y = Y, X

        X, Y = X+X, Y-X        
        min_ = min(X, Y, TOTAL - (X+Y))
        max_ = max(X, Y, TOTAL - (X+Y))
        if visited[min_][max_]:
            continue
        q.append((min_, max_))
        visited[min_][max_] = True
print(0)