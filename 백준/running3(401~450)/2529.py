k = int(input())
signs = list(input().split())
visited = [0] * 10
r = []

def check(a, b, op):
    if op == '<' and a > b: return False
    if op == '>' and a < b: return False
    return True

def dfs(c, n):
    if c == k + 1:
        r.append(n)
        return
    
    for i in range(10):
        if visited[i]: continue
        if c == 0 or check(n[c-1], str(i), signs[c-1]):
            visited[i] = 1
            dfs(c+1, n+str(i))
            visited[i] = 0

dfs(0, '')
r.sort()
print(r[-1])
print(r[0])

