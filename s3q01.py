import sys
sys.stdin=open("input.txt","rt")
n, m = map(int,input().split())
data = list(map(int, input().split()))
data.sort()
lt=0
rt=n-1
while lt<=rt:
  mid=(lt+rt)//2
  if data[mid]==m:
    print(mid+1)
    break
  elif data[mid]>m:
    rt=mid-1
  else:
    lt=mid+1

#new mycode
import sys
#sys.stdin = open('input.txt', 'rt')
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
lt = 0
rt = n-1
while lt <= rt:
    mid = (lt + rt) // 2
    if data[mid] > m:
        rt = mid-1
    elif data[mid] == m:
        print(mid+1)
        break
    elif data[mid] < m:
        lt = mid + 1
