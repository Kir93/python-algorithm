import sys

r, c = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

if r % 2 == 1:
    print(('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1))
elif c % 2 == 1:
    print(('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1))
elif r % 2 == 0 and c % 2 == 0:
    low = 1000
    position = [-1, -1]

    for i in range(r):
        if i % 2 == 0:
            for j in range(1, c, 2):
                if low > ground[i][j]:
                    low = ground[i][j]
                    position = [i, j]
        else:  # i % 2 == 1
            for j in range(0, c, 2):
                if low > ground[i][j]:
                    low = ground[i][j]
                    position = [i, j]

    res = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (position[1] // 2)
    x = 2 * (position[1] // 2)
    y = 0
    xbound = 2 * (position[1] // 2) + 1

    while x != xbound or y != r - 1:
        if x < xbound and [y, xbound] != position:
            x += 1
            res += 'R'
        elif x == xbound and [y, xbound - 1] != position:
            x -= 1
            res += 'L'
        if y != r - 1:
            y += 1
            res += 'D'

    res += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - position[1] - 1) // 2)

    print(res)