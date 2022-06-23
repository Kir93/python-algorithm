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

#best code
import sys
sys.stdin=open("input.txt", "r")
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n=map(int, input().split())
Line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)

#new mycode
import sys
#sys.stdin = open('input.txt', 'rt')
k, n = map(int, input().split())
data = []
for _ in range(k):
    data.append(int(input()))
lt = 1
rt = max(data)
r = -999999
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    for x in data:
        cnt += x // mid
    if cnt >= n and mid > r:
        r = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(r)

