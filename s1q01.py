import sys
sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)

#nextCode
import sys
#sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
data = []

for i in range(1, n+1):
    if(n % i == 0):
        data.append(i)

if(k > len(data)):
    print(-1)
else:
    print(data[k-1])
