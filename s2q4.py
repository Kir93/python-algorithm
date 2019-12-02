import sys
#sys.stdin=open("input.txt","rt")
n = int(input())
data1 = list(map(int,input().split()))
n = int(input())
data2 = list(map(int,input().split()))
data = data1 + data2
data.sort()

for x in data:
  print(x, end=' ')
