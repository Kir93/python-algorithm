import sys
from collections import deque

input = sys.stdin.readline
ROOT = 26
LEAF = 27
FAIL_NODE = 28
LENGTH = 29
CHILDREN_SIZE = 26
WHOLE_SIZE = 30
STEP = 30


def insert(word):
    node = root

    for char in word:
        index = ord(char) - 97

        if node[index] is None:
            next_node = [None] * WHOLE_SIZE
            next_node[LENGTH] = node[LENGTH] + 1
            next_node[FAIL_NODE] = node
            node[index] = next_node

        node = node[index]

    node[LEAF] = True


def make_failure_table():
    queue = deque([root])

    while queue:
        node = queue.popleft()

        for i in range(CHILDREN_SIZE):
            next_node = node[i]

            if next_node is None:
                continue

            if node[ROOT]:
                next_node[FAIL_NODE] = root
            else:
                fail_node = node[FAIL_NODE]

                while not fail_node[ROOT] and fail_node[i] is None:
                    fail_node = fail_node[FAIL_NODE]

                if fail_node[i] is not None:
                    fail_node = fail_node[i]

                next_node[FAIL_NODE] = fail_node

            if not next_node[LEAF] and next_node[FAIL_NODE][LEAF]:
                next_node[LEAF] = True
                next_node[LENGTH] = next_node[FAIL_NODE][LENGTH]

            queue.append(next_node)


def search(word):
    node = root

    for i, char in enumerate(word):
        index = ord(char) - 97

        while not node[ROOT] and node[index] is None:
            node = node[FAIL_NODE]

        if node[index] is not None:
            node = node[index]

        if node[LEAF]:
            visited[i] = max(visited[i], node[LENGTH])


n = int(input())
street = input().rstrip()
tiles = [input().rstrip() for _ in range(int(input()))]
visited = [0] * n

for start in range(0, len(tiles), STEP):
    root = [None] * WHOLE_SIZE
    root[ROOT] = True
    root[LENGTH] = 0

    for i in range(start, min(start + STEP, len(tiles))):
        insert(tiles[i])

    make_failure_table()
    search(street)

delete_count, total = 0, 0

for i in range(n - 1, -1, -1):
    delete_count = max(delete_count, visited[i])

    if delete_count > 0:
        delete_count -= 1
    else:
        total += 1

print(total)