#mycode
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
data = list(map(int,input().split()))
score = [0 for i in data]
SUM = 0
for i in range(len(data)):
    if data[i] == 1:
        score[i] += data[i] + score[i-1]

for i in score:
    SUM += i

print(SUM)

#bestcode
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
cnt=0
sum=0
for i in range(n):
    if a[i]==1:
        cnt=cnt+1
        sum=sum+cnt
    else:
        cnt=0

print(sum)
