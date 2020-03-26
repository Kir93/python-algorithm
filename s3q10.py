#my code
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
data = list(map(int,input().split()))
sortData = [0 for _ in range(n)]
for i in range(n):
    cnt = 0
    for j in range(n):
        if data[i] == cnt:
            if sortData[j] == 0:
                sortData[j] = i+1
                break
        else:
            if sortData[j] == 0:
                cnt += 1

for x in sortData:
    print(x, end=' ')
    
#best code
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
seq=[0]*n
for i in range(n):
    for j in range(n):
        if(a[i]==0 and seq[j]==0):
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x, end=' ')
    
#new mycode
import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
data = list(map(int, input().split()))
tmp = [0] * n

for i in range(n):
    for j in range(n):
        if data[i] == 0:
            if tmp[j] == 0:
                tmp[j] = i+1
                break
        else:
            if tmp[j] == 0:
                data[i] -= 1
for x in tmp:
    print(x, end=' ')
