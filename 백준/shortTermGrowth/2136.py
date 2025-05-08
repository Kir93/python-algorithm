import sys; input = sys.stdin.readline
from collections import deque

def solve():
    N, P = map(int, input().split())

    # 정점 분할
    # 상태가 들어오는 in 노드는 i, 상태를 내보내는 out 노드는 i + N
    # 그러므로 전체 필요한 정점 수는 N * 2
    length = N * 2
    flow = [[0] * length for _ in range(length)]
    capacity = [[0] * length for _ in range(length)]
    connect = [[] for _ in range(length)]
    # in과 out을 연결
    for i in range(N):
        connect[i].append(i + N)
        connect[i + N].append(i)
        capacity[i][i + N] = 1
    # 길의 양 정점을 in과 out을 잘 구분하여 연결
    for _ in range(P):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        # a -> b
        connect[a + N].append(b)
        connect[b].append(a + N)
        capacity[a + N][b] = 1
        # b -> a
        connect[b + N].append(a)
        connect[a].append(b + N)
        capacity[b + N][a] = 1

    # 시작은 1, 끝은 2 (양방향이므로 1 -> 2나 2 -> 1나 똑같으므로 1 -> 2로 가는 루트를 전부 세어준다.)
    # 시작이 out이므로 0 + N = N
    # 끝은 in이므로 1 그대로
    start = N; end = 1
    answer = 0
    while True: # 최대 유량 알고리즘 시작
        prev = [-1] * length
        queue = deque([start])
        while queue:
            here = queue.popleft()
            if here == end:
                break
            for there in connect[here]:
                if capacity[here][there] - flow[here][there] > 0 and prev[there] == -1:
                    prev[there] = here
                    queue.append(there)
        if prev[end] == -1:
            break
        # 유량은 어차피 1
        here = end
        while here != start:
            flow[prev[here]][here] += 1
            flow[here][prev[here]] -= 1
            here = prev[here]
        answer += 1
    print(answer)

solve()