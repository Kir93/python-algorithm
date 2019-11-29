import sys
#sys.stdin=open("input.txt","rt")

def digit_sum(x):
  SUM = 0
  for i in x:
      SUM += int(i)
  return SUM

n = int(input())
data = list(input().split())
MAX = -99999
for idx, i in enumerate(data):
    temp = digit_sum(i)
    if MAX < temp:
        MAX = temp
        num = idx

print(data[num])
