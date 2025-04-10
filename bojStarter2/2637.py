import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
connect = [[] for _ in range(n + 1)]  # 연결 정보
needs = [[0] * (n + 1) for _ in range(n + 1)]  # 각 제품을 만들때 필요한 부품
q = deque()  # 위상 정렬
degree = [0] * (n + 1)  # 진입 차수
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    connect[b].append((a, c))
    degree[a] += 1

for i in range(1, n + 1):
    # 진입 차수가 0인걸 넣어준다.
    if degree[i] == 0:
        q.append(i)
# 위상 정렬 시작
while q:
    now = q.popleft()
    # 현 제품의 다음 단계 번호, 현 제품이 얼마나 필요한지
    for next, next_need in connect[now]:
        # 만약 현 제품이 기본 부품이면
        if needs[now].count(0) == n + 1:
            needs[next][now] += next_need
        # 현 제품이 중간 부품이면
        else:
            for i in range(1, n + 1):
                needs[next][i] += needs[now][i] * next_need
        # 차수 -1
        degree[next] -= 1
        if degree[next] == 0:
            # 차수 0이면 큐에 넣음
            q.append(next)
for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)
print(needs)