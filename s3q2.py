import sys
#sys.stdin = open("input.txt", "rt")
k, n = map(int,input().split())
data = []
for _ in range(k):
    data.append(int(input()))
data.sort()
lt=1
rt=data[-1]
res = 0
while lt<=rt:
    mid = (lt + rt) // 2
    c = 0
    for x in data:
        c+= x//mid
    if c >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
