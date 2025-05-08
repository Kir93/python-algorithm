import sys

input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = L[start]
        return

    init(node * 2, start, (start + end) // 2)
    init(node * 2 + 1, (start + end) // 2 + 1, end)

    tree[node] = tree[node * 2] * tree[node * 2 + 1]


def update(node, start, end, index, value):
    if index < start or index > end:
        return

    if start == end:

        if value > 0 :
            tree[node] = 1
        elif value == 0:
            tree[node] = 0
        else:
            tree[node] = -1

        return
    update(node * 2, start, (start + end) // 2, index, value)
    update(node * 2 + 1, (start + end) // 2 + 1, end, index, value)

    check = tree[node * 2] * tree[node * 2 + 1]

    if check > 0:
        tree[node] = 1
    elif check == 0:
        tree[node] = 0
    else:
        tree[node] = -1


def query(node, start, end, left, right):
    if left > end or right < start:
        return 1

    if left <= start and right >= end:  # 포함하고 있다면.

        if tree[node] > 0:
            tree[node] = 1
            return 1
        elif tree[node] == 0:
            tree[node] = 0
            return 0
        else:
            tree[node] = -1
            return -1

    return query(node * 2, start, (start + end) // 2, left, right) * query(node * 2 + 1, (start + end) // 2 + 1, end,left, right)


while True:
    try:
        N, K = map(int, input().split())
        L = list(map(int, input().split()))
        tree = [0] * (4 * N)

        init(1, 0, N - 1)

        Answer = ""

        for i in range(K):
            Q, A, B = input().split()

            A = int(A);
            B = int(B)

            if Q == "C":
                update(1, 0, N - 1, A - 1, B)
            else:
                check = query(1, 0, N - 1, A - 1, B - 1)
                if check == 0:
                    Answer += "0"
                elif check > 0:
                    Answer += "+"
                else:
                    Answer += "-"

        print(Answer)

    except:
        break