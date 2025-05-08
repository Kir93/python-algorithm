import sys
#sys.stdin = open("input.txt", "rt")
n,m = map(int,input().split())
data = list(map(int,input().split()))
lt=0
rt=1
r=data[0]
cnt = 0
while lt<=rt:
    if r<m:
        if rt<n:
            r+=data[rt]
            rt+=1
        else:
            break
    elif r==m:
        cnt += 1
        r-=data[lt]
        lt+=1
    else:
        r -= data[lt]
        lt+=1

print(cnt)
