n, m = map(int, input().split())
c = [input() for _ in range(n)]

empty_rows = 0
for i in range(n):
    if 'X' not in c[i]:
        empty_rows += 1

empty_cols = 0
for j in range(m):
    has_x = False
    for i in range(n):
        if c[i][j] == 'X':
            has_x = True
            break
    if not has_x:
        empty_cols += 1

print(max(empty_rows, empty_cols))