# from itertools import permutations
# n = int(input())
# for i in permutations([j for j in range(1, n+1)]):
#     print(*i)

n = int(input())
ls = [i for i in range(1, n+1)]
r = []
def dfs(dep):
    if dep == n: return print(*r)
    for i in range(n):
        if ls[i] not in r:
            r.append(ls[i])
            dfs(dep+1)
            r.pop()
dfs(0)