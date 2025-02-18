import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def SCC(node):
    global idx, scc_num
    visit[node] = idx
    root = idx
    idx += 1
    stack.append(node)

    for nxt in graph[node]:
        if not visit[nxt]:
            root = min(root, SCC(nxt))
        elif not check[nxt]:
            root = min(root, visit[nxt])

    if root == visit[node]:
        while stack:
            top = stack.pop()
            check[top] = 1
            scc_arr[top] = scc_num
            if node == top:
                break

        scc_num += 1

    return root

def neg(a):
    if a <= N: return a + N
    else: return a - N

# main part
N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(2 * N + 1)]
for _ in range(M):
    # R -> true, B -> false
    a, RB1, b, RB2, c, RB3 = list(input().rstrip().split())
    a, b, c = map(int, [a, b, c])
    if RB1 == 'B': a = a + N
    if RB2 == 'B': b = b + N
    if RB3 == 'B': c = c + N
    graph[neg(a)].append(b)
    graph[neg(b)].append(a)
    graph[neg(b)].append(c)
    graph[neg(c)].append(b)
    graph[neg(c)].append(a)
    graph[neg(a)].append(c)

# 타잔 알고리즘
idx = scc_num = 0
check = [False for _ in range(2 * N + 1)]
scc_arr = [0 for _ in range(2 * N + 1)]
visit = [0 for _ in range(2 * N + 1)]
stack = []
for i in range(1, 2 * N + 1):
    if check[i]: continue
    SCC(i)

for i in range(1, N + 1):
    if scc_arr[i] == scc_arr[i + N]:
        print(-1)
        exit(0)

for i in range(1, N + 1):
    if scc_arr[i] > scc_arr[i + N]:
        print('B', end='')
    else:
        print('R', end='')