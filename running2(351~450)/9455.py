for _ in range(int(input())):
    m, n = map(int, input().split())
    grid = [[] for _ in range(n)]
    for i in range(m):
        a = list(input().split())
        for j in range(n):
            grid[j].append(a[j])
    r = 0
    for i in range(n):
        bn = grid[i].count('1')
        f = m - 1
        for j in range(m - 1, -1, -1):
            if grid[i][j] == '1':
                r += f - j
                f -= 1
    print(r)