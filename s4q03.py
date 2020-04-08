import sys
#sys.stdin = open("input.txt", "r")
s = input()
stack = []
res = ''

for x in s:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)

#new mycode
import sys
#sys.stdin = open("input.txt", "rt")
data = input()
d = []
r = ''
for x in data:
  if x == '+' or x == '-':
    while d and d[-1] != '(':
      r += d.pop()
    d.append(x)
  elif x == '*' or x == '/':
    while d and (d[-1] == '*' or d[-1] == '/'):
      r += d.pop()
    d.append(x)
  elif x == '(':
    d.append(x)
  elif x == ')':
    while d and d[-1] != '(':
      r += d.pop()
    d.pop()
  else:
    r += x

while d:
  r += d.pop()
print(r)
