import sys
def fibonacci(n):
  val = [0]
  for i in range(1,n+1):
    if i==1:  val.append(1)
    elif i==2:  val.append(1)
    else:
      val.append(val[i-1]+val[i-2])
  return val[n]

n = int(sys.stdin.readline())
print(fibonacci(n))
