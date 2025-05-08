import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    files = [*map(int, input().split())]
    minCost = [[0]*K for _ in range(K)]
    
    subSum = {-1: 0}
    for idx in range(K):
        subSum[idx] = subSum[idx-1] + files[idx]
    
    for size in range(1, K):
        for start in range(K-1):
            end = start + size
            
            if end >= len(files):
                break
            
            result = float("inf")
            for cut in range(start, end):
                result = min(result, minCost[start][cut] + minCost[cut+1][end] + subSum[end] - subSum[start-1])
            
            minCost[start][end] = result

    print(minCost[0][-1])