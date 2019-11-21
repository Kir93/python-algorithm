import sys
def dp(n):
  val =[[0 for x in range(2)] for y in range(n+1)]
  for i in range(1,n+1):
    if i == 1:
      val[i][0] = 2
    elif i == 2:
      val[i][0] = 7
      val[i][1] = 1
    else:
        val[i][1] = (val[i-1][1] + val[i-3][0]) % 1000000007
        val[i][0] = (3*val[i-2][0] + 2*val[i-1][0] + 2*val[i][1]) % 1000000007
  return val[n][0]

n = int(sys.stdin.readline())
print(dp(n))
