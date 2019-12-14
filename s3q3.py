import sys
#sys.stdin = open("input.txt", "rt")
n,m = map(int,input().split())
data = list(map(int,input().split()))
def Count(mid):
    cnt = 0
    r=0
    for i in data:
        if r+i < mid:
            r += i
        else:
            cnt+=1
            r=i
    return cnt
lt=1
rt = sum(data)
res = 0
while(lt<=rt):
    mid = (lt + rt) // 2
    if Count(mid) >= m:
       res = mid
       lt = mid + 1
    else:
        rt = mid - 1

print(res)
