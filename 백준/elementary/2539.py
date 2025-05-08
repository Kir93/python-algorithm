import sys
n, m = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
q = int(sys.stdin.readline())
arr = []
left = 0
right = 9876543210
for _ in range(q):
    a, b = map(int, sys.stdin.readline().split())
    
    left = max(left, a)
    arr.append((a, b))

arr.sort(key=lambda x : (x[1]))

while left < right:
    mid = (left + right) // 2
    
    idx = 0
    
    cnt = 0
    while idx < q:
        cnt += 1
        start_x = arr[idx][1]
        

        start_y = 1
        i = idx
        

        while i < q and start_x <= arr[i][1] < start_x + mid and start_y <= arr[i][0] < start_y + mid:
            i += 1
            

        idx = i
        
    if cnt <= k:
        right = mid
    else:
        left = mid + 1
    
print(right)