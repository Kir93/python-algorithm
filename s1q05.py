import sys
# sys.stdin = open("input.txt", "rt")
n,m = map(int,input().split())
cnt = [0]*(n+m+1)
MAX = -99999
for i in range(1,n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in cnt:
    if i > MAX:
        MAX = i

for i in range(len(cnt)):
    if MAX == cnt[i]:
        print(i, end=' ')

#new mycode
import sys
#sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
cnt = [0] * (n+m+3)
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
for x in range(len(cnt)):
    if(max(cnt) == cnt[x]):
        print(x, end=" ")
