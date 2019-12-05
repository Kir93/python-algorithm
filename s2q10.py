import sys
sys.stdin=open("input.txt","rt")
n = 9
def check(a):
  for i in range(n):
    sum1=sum2=0
    for j in range(n):
      sum1 += data[i][j]
      sum2 += data[j][i]
    if sum1 != 45 or sum2 != 45:
      return False
  for i in range(3):
    for j in range(3):
      sum = 0
      for x in range(3):
        for y in range(3):
          sum += data[i*3 + x][j*3 + y]
      if sum != 45:
        return False
  return True

data = [list(map(int,input().split())) for _ in range(n)]
if check(data): print("YES")
else: print("NO")
