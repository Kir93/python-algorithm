n=int(input())
arr = list(map(int,input().split()))

LIS = [arr[0]]
dp = [(0,arr[0])] 

def binarySearch(e):
    start = 0
    end = len(LIS) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start


for i in range(1,n):
    if arr[i] > LIS[-1]:
        LIS.append(arr[i])
        dp.append((len(LIS)-1, arr[i]))

    else:
        idx = binarySearch(arr[i])
        LIS[idx] = arr[i]
        dp.append((idx, arr[i]))


print(len(LIS))

last_idx = len(LIS) - 1
res = []
for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == last_idx:
        res.append(dp[i][1])
        last_idx-=1

print(*res[::-1])