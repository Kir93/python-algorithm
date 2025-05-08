import sys
input = sys.stdin.readline

def get_sum(target):
    total = 0
    for i in range(N):
        if target >= arr[i][0]:
            total += ((min(arr[i][1],target) - arr[i][0])//arr[i][2]) + 1
    return total

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
left = 0
right = 2147483648
while left < right:
    mid = (left + right)//2
    if not get_sum(mid)&1:
        left = mid + 1
    else:
        right = mid
if left == 2147483648:
    print('NOTHING')
else:
    print(left,get_sum(left) - get_sum(left-1))