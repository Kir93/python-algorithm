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
