import sys
def dp(n):
  val = [0]
  for i in range(1,n+1):
    if i == 1:
      val.append(1)
    elif i == 2:
      val.append(3)
    else:
      val.append(val[i-1] + 2*val[i-2])
  return val[n]

n = int(sys.stdin.readline())
print(dp(n)%10007)
