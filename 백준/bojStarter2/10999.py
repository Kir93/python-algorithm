N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

tree = [0] * (4 * N)
lazy = [0] * (4 * N)

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]

def query(node, start, end, left, right):
    propagate(node, start, end)
    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    q1 = query(node * 2, start, mid, left, right) 
    q2 = query(node * 2 + 1, mid+1, end, left, right)
    return q1 + q2

def propagate(node, left, right):
    if lazy[node]:
        tree[node] += (right - left + 1) * lazy[node]

        if left != right:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0

def update(node, start, end, left, right, diff):
    propagate(node, start, end)
    if right < start or end < left:
        return 

    if left <= start and end <= right:
        lazy[node] += diff
        propagate(node, start, end)
        return 

    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, diff) 
    update(node * 2 + 1, mid+1, end, left, right, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    return 

init(1, 0, N-1)
for _ in range(M + K):
    cmd = tuple(map(int, input().split()))
    a, b, c = cmd[:3]
    b -= 1
    c -= 1
    if a == 1:
        d = cmd[3]
        update(1, 0, N-1, b, c, d)
    elif a == 2:
        print(query(1, 0, N-1, b, c))
