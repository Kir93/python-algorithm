import sys
input = sys.stdin.readline
INF = float("inf")

n = int(input())
m = int(input())
path = [[()]*(n+1) for _ in range(n+1)]
APSP = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    APSP[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    APSP[a][b] = min(APSP[a][b], c)
    path[a][b] = (a, b)
    
def floyd_warshall():
    for mid in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                cal_cost = APSP[i][mid] + APSP[mid][j]
                if cal_cost < APSP[i][j]:
                    APSP[i][j] = cal_cost
                    path[i][j] = path[i][mid] + path[mid][j][1:]
    return

floyd_warshall()

for i in range(1, n+1):
    line = []
    for j in range(1, n+1):
        if APSP[i][j] == INF:
            line.append(0)
        else:
            line.append(APSP[i][j])
    print(*line)

for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(path[i][j]), *path[i][j])