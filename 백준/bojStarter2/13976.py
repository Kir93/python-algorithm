import sys
input = sys.stdin.readline
mod = 1000000007

def multiply(A1,A2):
  result = [[0,0],[0,0]]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        result[i][j] += A1[i][k]*A2[k][j]
        result[i][j] %= mod
  return result

def cal(A,n):
  if n == 1:
    return A
  cal2 = cal(A,n//2)
  result = multiply(cal2,cal2)
  if n%2:
    return multiply(result,A)
  return result

N = int(input())
if N%2:
  print(0)
else:
  N //= 2
  A = [[4,-1],[1,0]]
  print(sum(cal(A,N)[0])%mod)