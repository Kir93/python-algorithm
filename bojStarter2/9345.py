import sys
import math
input = sys.stdin.readline


def getTreeLength():
    # 2의 제곱꼴인지 확인
    if N & (N - 1) == 0:
        return 2*N - 1
    else:
        return pow(2, math.ceil(math.log(N, 2)) + 1) - 1


def initializeSegmentTree(index, start, end):
    if start == end:
        tree[index] = (nums[start], nums[start])
        return

    mid = (start + end)//2
    initializeSegmentTree(index*2, start, mid)
    initializeSegmentTree(index*2+1, mid+1, end)
    tree[index] = (tree[index*2][0], tree[index*2+1][1])


def modifySegmentTree(index, target, value, start, end):
    if target < start or end < target:
        return

    if start == end:
        tree[index] = (value, value)
        return

    mid = (start + end)//2
    modifySegmentTree(index*2, target, value, start, mid)
    modifySegmentTree(index*2+1, target, value, mid+1, end)
    tree[index] = (min(tree[index*2][0], tree[index*2+1][0]), max(tree[index*2][1], tree[index*2+1][1]))


def queryInSegmentTree(index, range, start, end):
    if range[1] < start or end < range[0]:
        return True

    if range[0] <= start and end <= range[1]:
        return range[0] <= tree[index][0] and tree[index][1] <= range[1]

    mid = (start+end)//2
    return queryInSegmentTree(index*2, range, start, mid) and queryInSegmentTree(index*2+1, range, mid+1, end)


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    nums = [i for i in range(N+1)]

    tree = [(-1, -1)]*(getTreeLength())
    initializeSegmentTree(1, 1, N)

    for _ in range(K):
        q, a, b = map(int, input().split())
        a += 1
        b += 1

        if q == 0:
            # xchg
            modifySegmentTree(1, a, nums[b], 1, N)
            tmpA = nums[a]
            nums[a] = nums[b]
            modifySegmentTree(1, b, tmpA, 1, N)
            nums[b] = tmpA
        else:
            # query
            if queryInSegmentTree(1, (a, b), 1, N):
                print("YES")
            else:
                print("NO")