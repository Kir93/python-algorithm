n, k = map(int, input().strip().split(" "))

stones = {row:[] for row in range(1, 1+n)}
for _ in range(k):
    row, col = map(int, input().strip().split(" "))
    stones[row].append(col)

bipartite_matching = [False for _ in range(1+n)]

def dfs(i):

    if visited[i]:
        return False
    visited[i] = True

    for j in stones[i]:
        i_to_j = bipartite_matching[j]
        if i_to_j == False or dfs(i_to_j) == True:
            bipartite_matching[j] = i
            return True
    
    return False

c = 0
for i in range(1, 1+n):
    visited = [False for _ in range(1+n)]
    if dfs(i) :
        c += 1

print(c)