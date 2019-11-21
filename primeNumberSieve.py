import sys
def primeNumberSieve(n):
  val = [i for i in range(n+1)]
  for i in range(2,n+1):
    if val[i] == 0: continue
    for j in range(i+i,n+1,i):
      val[j] = 0
  for i in range(2,n+1):
    if val[i] != 0:
      print(val[i], end=' ')

n = int(sys.stdin.readline())
primeNumberSieve(n)
