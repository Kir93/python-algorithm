import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input()) # 정점의 개수

# 그래프 정보
graph = [[] for _ in range(n+1)]
for _ in range(n):
    tree = list(map(int, input().split()))
    for i in range(1, len(tree)//2):
        graph[tree[0]].append((tree[2*i-1], tree[2*i]))

# 방문 배열
visited = [-1] * (n+1)
visited[1] = 0  # 루트 노드 거리는 0으로 초기화

# DFS 함수
def DFS(x, distance):
    for i, w in graph[x]:
        # 아직 방문하지 않은 노드이면 현재까지의 거리 + 해당 노드까지의 가중치로 방문 배열 값을 변경
        if visited[i] == -1:
            visited[i] = distance + w
            DFS(i, distance + w)
            
DFS(1, 0) # 루트 노드(1)에서의 각 정점까지의 거리 계산
max_distance = max(visited) # 최장 거리
max_node = visited.index(max_distance) # 해당 노드


# max_node에서 시작해 각 정점까지의 거리 계산
visited = [-1] * (n+1)
visited[max_node] = 0 
DFS(max_node, 0)

print(max(visited))