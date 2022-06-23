import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
data = []
for i in range(n):
    s, e = map(int,input().split())
    data.append((s,e))
data.sort(reverse=True)
cnt=0
r=0
for h, w in data:
    if r<w:
        r=w
        cnt+=1

print(cnt)

#new mycode
import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
data = []
for _ in range(n):
    h, w = map(int, input().split())
    data.append((h, w))
data.sort(reverse=True)
ow = cnt = 0
for h, w in data:
    if ow < w:
        cnt += 1
        ow = w
print(cnt)
