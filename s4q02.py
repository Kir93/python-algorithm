import sys
#sys.stdin = open("input.txt", "r")
s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)

#new mycode
import sys
#sys.stdin = open("input.txt", "rt")
laser = input()
bar = []
res = 0
for i in range(len(laser)):
  if laser[i] == '(':
    bar.append(laser[i])
  else:
    if laser[i-1] == '(':
      bar.pop()
      res += len(bar)
    else:
      bar.pop()
      res += 1
print(res)
