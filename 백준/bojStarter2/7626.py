import sys
input = sys.stdin.readline
        
def segUpdate(left, right, s):    
    left += N
    right += N
    def update(node, s):
        count[node] += s
        old = stree1[node]
        if count[node] > 0:
            stree1[node] = stree0[node]
        elif node>N:
            stree1[node] = 0
        else:
            stree1[node] = stree1[node<<1] + stree1[node<<1|1]
        if stree1[node] == old: return
        while node>=2:
            node >>= 1
            if count[node] > 0: break
            stree1[node] = stree1[node<<1] + stree1[node<<1|1]
    
    while left <= right:
        if left % 2 == 1 or left > N:
            update(left, s)
            left += 1
        if left > right: continue
        if right % 2 == 0 or right > N:
            update(right, s)
            right -= 1
        left >>= 1
        right >>= 1

xsyy, yy = [], []
for i in range(int(input())):
    x1, x2, y1, y2 = map(int,input().split())
#    x1, y1, x2, y2 = map(int,input().split()) 화성지도
    xsyy.append([x1, 1, y1, y2])
    xsyy.append([x2, -1, y1, y2])
    yy.append(y1)
    yy.append(y2)

xsyy.sort()
yy=list(set(yy))
yy.sort()
ylist = {y:i for i, y in enumerate(yy)}

N = len(yy)
stree0 = [0] * (2*N)
stree1 = [0] * (2*N)
count = [0] * (2*N)
for i in range(1, N): stree0[N+i] = yy[i] - yy[i-1]
for i in range(N-1, 0, -1): stree0[i] = stree0[i<<1] + stree0[i<<1|1]

area, xold = 0, xsyy[0][0]
for x, s, y1, y2 in xsyy:
    area += (x-xold) * stree1[1]
    segUpdate(ylist[y1]+1, ylist[y2], s)
    xold = x
print(area)