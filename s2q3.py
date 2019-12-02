import sys
sys.stdin=open("input.txt","rt")
data = [i for i in range(21)]
for _ in range(10):
  a, b = map(int,input().split())
  for i in range((b-a+1)//2):
    data[a+i], data[b-i] = data[b-i], data[a+i]

for i in range(1,21):
  print(data[i], end=' ')
