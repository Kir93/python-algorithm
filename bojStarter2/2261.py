import sys
n = int(input())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr.sort()

def get_dist(a, b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def get_min(start, end):
    if start == end: 
        return sys.maxsize

    if end - start == 1: 
        return get_dist(arr[start], arr[end])

    mid = (start + end) // 2 

    min_dist = min(get_min(start, mid), get_min(mid, end))

    candidates = []
    for i in range(start, end+1):
        if (arr[mid][0] - arr[i][0])**2 < min_dist:
            candidates.append(arr[i])

    candidates.sort(key=lambda x: x[1])

    for i in range(len(candidates)-1):
        for j in range(i+1, len(candidates)):
        
            if (candidates[i][1] - candidates[j][1])**2 < min_dist:
                min_dist = min(min_dist, get_dist(
                    candidates[i], candidates[j]))
            else:
                break

    return min_dist


print(get_min(0, n-1))