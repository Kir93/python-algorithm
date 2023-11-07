from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while True:
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                if board[nx][ny] == "*":
                    break
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]
            print(visited)


if __name__ == "__main__":
    m, n = map(int, input().split())
    board = [input() for _ in range(n)]

    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    C = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == "C":
                C.append((i, j))
    (sx, sy), (ex, ey) = C

    visited = [[float("inf")] * m for _ in range(n)]
    bfs(sx, sy)

    print(visited[ex][ey] - 1)