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
for i in data:
    temp = digit_sum(i)
    if MAX < temp:
        MAX = temp
        num = i

print(i)


'''
import sys
sys.stdin=open("input.txt", "r")
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

n=int(input())
a=list(map(int, input().split()))
res=0
max=-2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)
'''
