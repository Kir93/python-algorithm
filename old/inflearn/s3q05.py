import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
data = []
for i in range(n):
    s, e = map(int,input().split())
    data.append((s,e))

data.sort(key=lambda x : (x[1],x[0]))
ep = 0
cnt = 0
for s, e in data:
    if ep<=s:
        ep=e
        cnt+=1

print(cnt)

#new mycode
import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
data = []
for _ in range(n):
    s, e = map(int, input().split())
    data.append((s, e))
data.sort(key=lambda x: x[1])
cnt = 0
oe = 0
for s, e in data:
    if oe <= s:
        cnt += 1
        oe = e
print(cnt)
