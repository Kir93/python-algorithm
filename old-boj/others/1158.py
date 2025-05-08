from collections import deque
ls = deque()
n, k = map(int, input().split())
for i in range(1, n+1): ls.append(i)
r = []
while ls:
    if len(ls) != 1: 
        ls.rotate(-k+1)
        r.append(ls.popleft())
    else: r.append(ls.pop())        
print(str(r).replace('[', '<').replace(']', '>'))
