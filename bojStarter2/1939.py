from collections import deque
import sys

input = sys.stdin.readline


def bfs(mid):
    visited[start] = 1
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if now == end:
            return True
        for nx, nc in graph[now]:
            if visited[nx] == 0 and mid <= nc:
                q.append(nx)
                visited[nx] = 1

    return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    for i in range(1, n + 1):
        graph[i].sort(reverse=True)

    start, end = map(int, input().split())
    low, high = 1, 1000000000
    while low <= high:
        visited = [0 for _ in range(n + 1)]
        mid = (low + high) // 2
        if bfs(mid):
            low = mid + 1
        else:
            high = mid - 1

    print(high)