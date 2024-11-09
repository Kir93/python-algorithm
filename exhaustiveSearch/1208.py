import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def getNum(arr, find):
    return bisect_right(arr, find) - bisect_left(arr, find)

def getSum(arr, sumArr):
    for i in range(1, len(arr) + 1):
        for a in combinations(arr, i):
            sumArr.append(sum(a))
    sumArr.sort()

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = arr[:n//2], arr[n//2:]
leftSum, rightSum = [], []

getSum(left, leftSum)
getSum(right, rightSum)
ans = 0
for l in leftSum:
    find = s - l
    ans += getNum(rightSum, find)

ans += getNum(leftSum, s)
ans += getNum(rightSum, s)

print(ans)