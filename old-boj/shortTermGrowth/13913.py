from collections import deque
N, K = map(int,input().split())
visited = [False] * (200001)

def bfs(n):

    deq = deque()
    deq.append([n, 0,[n]])
    visited[n] = True

    if n > K:
        return n - K, [int(x) for x in range(n,K - 1,-1)]


    while deq:
        x, count, road = deq.popleft()

        if x == K:
            return count, road

        arr = [x - 1, x + 1, x * 2]
        for a in arr:
            if 0 <= a <= 100000 and visited[a] == False:
                visited[a] = True
                r = road + [a]
                deq.append([a, count + 1, r])

ans_count, ans_road = bfs(N)

print(ans_count)
for path in ans_road:
    print(path,end=' ')