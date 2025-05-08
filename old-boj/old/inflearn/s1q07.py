import sys
#sys.stdin=open("input.txt","rt")
n = int(input())
a = [0] * (n+1)
cnt = 0

for i in range(2,n+1):
    if a[i]==0:
        cnt += 1
    for j in range(i,n+1,i):
        a[j] = 1

print(cnt)

#new mycode
import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
cnt = [0] * (n+3)
res = 0
for i in range(2, n+1):
    if cnt[i] == 0:
        res += 1
        for j in range(i, n+1, i):
            cnt[j] = 2
print(res)
