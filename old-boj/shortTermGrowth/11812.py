import sys
input = sys.stdin.readline

def max_level(level):
    if level <= 0:
        return 0

    if k == 1:
        return level

    return (k**level - 1) // (k - 1)

def find_my_level(node):
    i = 1
    while True:
        if max_level(i) >= node:
            return i

        i += 1

def find_parent(node, node_level):
    if node == 1:
        return -1

    my_num_in_level = node - max_level(node_level - 1)

    parent = ((my_num_in_level - 1) // k) + max_level(node_level - 2) + 1

    return parent

n, k ,q = map(int, input().split())

for _ in range(q):
    x, y = map(int, input().split())

    if k == 1:
        print(abs(x - y))
        continue

    x_level = find_my_level(x)
    y_level = find_my_level(y)

    distance = abs(x_level - y_level)
    if x_level > y_level:
        while True:
            if x_level == y_level:
                break

            x = find_parent(x, x_level)
            x_level -= 1

    elif y_level > x_level:
        while True:
            if y_level == x_level:
                break

            y = find_parent(y, y_level)
            y_level -= 1

    while True:
        if x == y:
            break

        x = find_parent(x, x_level)
        x_level -= 1
        y = find_parent(y, y_level)
        y_level -= 1
        distance += 2

    print(distance)