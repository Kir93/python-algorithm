n, m = map(int, input().split())

rectangle_input = [[0 for _ in range(m + 1)]]

for _ in range(n):
    line_input = [0] + list(map(int, list(input())))
    rectangle_input.append(line_input)

ans = 0

s = [[0 for _ in range(m+1)] for _ in range(n+1)]

for row in range(1, n + 1):
    for col in range(1, m + 1):
        s[row][col] = s[row - 1][col] + s[row][col - 1] - s[row - 1][col - 1] + rectangle_input[row][col]

def sum_cal(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]

for i in range(1, m-1):
    for j in range(i+1, m):
        r1 = sum_cal(1, 1, n, i)
        r2 = sum_cal(1, i+1, n, j)
        r3 = sum_cal(1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(1, n-1):
    for j in range(i+1, n):
        r1 = sum_cal(1, 1, i, m)
        r2 = sum_cal(i+1, 1, j, m)
        r3 = sum_cal(j+1, 1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(1, m):
    for j in range(1, n):
        r1 = sum_cal(1, 1, n, i)
        r2 = sum_cal(1, i+1, j, m)
        r3 = sum_cal(j+1, i+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(i+1, 1, n, j)
        r3 = sum_cal(1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, m)
        r2 = sum_cal(i+1, 1, n, j)
        r3 = sum_cal(i+1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(1, j+1, i, m)
        r3 = sum_cal(i+1, 1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

print(ans)