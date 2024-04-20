import sys
input = sys.stdin.readline

n = int(input())
tree = [0]*(4*10**6)

def putCandy(left, right, node, b, c):
    tree[node] += c
    if left == right:
        return
    mid = (left+right) // 2
    if b <= mid:

        putCandy(left, mid, node*2, b, c)
    else:

        putCandy(mid+1, right, node*2+1, b, c)
    
def findCandy(left, right, node, b):
    tree[node] -= 1 
    if left == right:

        return left
    mid = (left+right) // 2 
    if tree[node*2] >= b:

        return findCandy(left, mid, node*2, b)
    else:

        return findCandy(mid+1, right, node*2+1, b-tree[node*2])
    
for _ in range(n):
    line = list(map(int, input().rstrip().split()))
    if len(line) == 2:
        b = line[1]
        print(findCandy(1, 10**6, 1, b))
    elif len(line) == 3:
        _, b, c = line
        putCandy(1, 10**6, 1, b, c)