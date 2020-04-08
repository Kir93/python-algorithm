import sys
sys.stdin = open("input.txt", "rt")
s = input()
stack = []
a=b=c=0
for x in s:
  if x.isdecimal():
    stack.append(int(x))
  else:
    b=stack.pop()
    a=stack.pop()
    if x == '+':
      c = a+b
      stack.append(c)
    elif x == '-':
      c = a-b
      stack.append(c)
    elif x == '*':
      c = a*b
      stack.append(c)
    elif x == '/':
      c = a/b
      stack.append(c)

print(stack.pop())

#new mycode
import sys
#sys.stdin = open("input.txt", "rt")
data = input()
d = []
for x in data:
  if x.isdecimal():
    d.append(int(x))
  else:
    b = d.pop()
    a = d.pop()
    if x == '+':
      d.append(a + b)
    elif x == '-':
      d.append(a - b)
    elif x == '*':
      d.append(a * b)
    elif x == '/':
      d.append(a / b)

print(d.pop())
