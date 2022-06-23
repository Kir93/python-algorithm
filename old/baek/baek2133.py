import sys
def dp(n):
  val = [1]
  for i in range(1,n+1):
    if i == 1:
      val.append(0)
    elif i == 2:
      val.append(3)
    elif i%2 == 1:
      val.append(0)
    else:
      val.append((3*val[i-2]))
      for j in range(4,i+1,2):
        val[i] += 2*val[i-j]
  return val[n]

n = int(sys.stdin.readline())
print(dp(n))
