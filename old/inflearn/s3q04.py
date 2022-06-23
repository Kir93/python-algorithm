#my code
import sys
#sys.stdin = open("input.txt", "rt")
n,c = map(int,input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
lt = data[0]
rt = data[-1]
res = 0
def count(mid):
    cnt = 1
    i=0
    j=1
    while(j<len(data)):
        if (data[j] - data[i]) >= mid:
            i = j
            j += 1
            cnt += 1
        else:
            j += 1
    return cnt

while(lt<=rt):
    mid = (lt + rt) // 2
    if count(mid) >= c:
       res = mid
       lt = mid + 1
    else:
        rt = mid - 1

print(res)

#best code
import sys
sys.stdin=open("input.txt", "r")
def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)

#new code
import sys
#sys.stdin = open('input.txt', 'rt')
n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
lt = 1
rt = data[-1]
res = 0
while lt <= rt:
    cnt = 1
    mid = (lt + rt) // 2
    r = data[0]
    for i in range(1, n):
        if data[i] - r >= mid:
            cnt += 1
            r = data[i]
    if cnt >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
