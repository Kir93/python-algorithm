import sys
#sys.stdin = open("input.txt", "r")
num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []
for i in num:
    while stack and m > 0 and stack[-1] < i:
        stack.pop()
        m -= 1
    stack.append(i)
if m != 0:
    stack = stack[:-m]

num = ''.join(map(str, stack))

print(num)

#new mycode
import sys
#sys.stdin = open("input.txt", "rt")
n, m = input().split()
m = int(m)
d = []
for x in n:
  while d and d[-1] < int(x) and m > 0:
    d.pop()
    m -= 1
  d.append(int(x))
if m != 0:
  d = d[:-m]
for x in d:
  print(x, end='')
  
