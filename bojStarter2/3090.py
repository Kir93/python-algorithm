import sys, copy
input = sys.stdin.readline
 
N, T = map(int, input().split())
arr = list(map(int, input().split()))
 
 
def investigate(gap):
    global tempArr
    tempArr = copy.deepcopy(arr)
    operCount = 0
 
    for i in range(N - 1):
        if tempArr[i + 1] - tempArr[i] > gap:
            operCount += tempArr[i + 1] - (tempArr[i] + gap)
            tempArr[i + 1] = tempArr[i] + gap
    
    for i in range(N - 1, 0, -1):
        if tempArr[i - 1] - tempArr[i] > gap:
            operCount += tempArr[i - 1] - (tempArr[i] + gap)
            tempArr[i - 1] = tempArr[i] + gap
    
    if operCount <= T:
        return True
    return False
 
 
left = 0
right = 1000000000
result = []
 
while left <= right:
    mid = (left + right) // 2
 
    if investigate(mid):
        result = copy.deepcopy(tempArr)
        right = mid - 1
    else:
        left = mid + 1
 
print(*result)