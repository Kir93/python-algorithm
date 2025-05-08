import sys
import math
 
def init_tree(start, end, index):
    if start == end:
        tree[index] = arr[start]
    else:
        mid = (start + end) // 2
        tree[index] = init_tree(start, mid, 2*index) * init_tree(mid+1, end, 2*index + 1) % 1000000007
    return tree[index]
 
def find_mul(start, end, index, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[index]
 
    mid = (start + end) // 2
    return find_mul(start, mid, 2*index, left, right) * find_mul(mid+1, end, 2*index + 1, left, right) % 1000000007
 
def update_tree(start, end, index, where, diff):
    if where < start or end < where:
        return
 
    if start == end:
        tree[index] = diff
    else:
        mid = (start + end) // 2
        update_tree(start, mid, index*2, where, diff)
        update_tree(mid+1, end, index*2 + 1, where, diff)
        tree[index] = tree[2*index] * tree[2*index + 1] % 1000000007
 
N, M, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))
init_tree(0, N-1, 1)
 
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
 
    if a == 1:
        update_tree(0, N-1, 1, b-1, c)
 
    else:
        print(find_mul(0, N-1, 1, b-1, c-1))