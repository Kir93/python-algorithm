import sys
from math import ceil, log
input = lambda: sys.stdin.readline().rstrip()

def mid(l, r):
    return (l+r) // 2

###############################################

def init(l, r, node):
    if l == r:
        segment_tree[node] = arr[l]
        return
    init(l, mid(l,r), node*2)
    init(mid(l,r)+1, r, node*2+1)
    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2+1]

def update(l, r, node, IDX, DIFF):
    if not (l <= IDX <= r):
        return
    segment_tree[node] += DIFF
    if l == r:
        return
    update(l, mid(l,r), node*2, IDX, DIFF)
    update(mid(l,r)+1, r, node*2+1, IDX, DIFF)

def interval_sum(l, r, node, LEFT, RIGHT):
    if r < LEFT or RIGHT < l: # [l, r]이 [LEFT, RIGHT]를 완전히 벗어남. 
        return 0
    if LEFT <= l and r <= RIGHT: # [l, r]이 [LEFT, RIGHT] 안에 완전히 포함됨. 
        return segment_tree[node]
    lsum = interval_sum(l, mid(l,r), node*2, LEFT, RIGHT)
    rsum = interval_sum(mid(l,r)+1, r, node*2+1, LEFT, RIGHT)
    return lsum + rsum

###############################################

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    
    segment_tree = [0] * (2**ceil(log(m+n, 2)+1)) # <= 4N
    arr = [0]*m + [1]*n
    pos = [0] + [i+m for i in range(n)] # 영화의 번호는 1-indexed
    init(0, m+n-1, 1)
    
    moves = list(map(int, input().split()))
    latest = m-1
    for i in moves:
        update(0, m+n-1, 1, pos[i], -1)
        print(interval_sum(0, m+n-1, 1, 0, pos[i]-1), end=' ')
        pos[i] = latest
        latest -= 1
        update(0, m+n-1, 1, pos[i], +1)


    print()
