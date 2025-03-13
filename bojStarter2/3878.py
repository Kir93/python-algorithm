import sys
from functools import cmp_to_key

def bcmpccw(a,b): #벡터 base-a, base-b의 외적, ccw:1 cw:-1 0이면 a가 짧으면:1, 길면: -1 반환
    v1=[a[0]-bbase[0],a[1]-bbase[1]]
    v2=[b[0]-bbase[0],b[1]-bbase[1]]
    if (v1[0]*v2[1])-(v1[1]*v2[0])>0:
        return 1
    elif (v1[0]*v2[1])-(v1[1]*v2[0])<0:
        return -1
    else:
        if (v1[0]**2+v1[1]**2)>(v2[0]**2+v2[1]**2):
            return -1
        else:
            return 1

def wcmpccw(a,b): #벡터 base-a, base-b의 외적, ccw:1 cw:-1 0이면 a가 짧으면:1, 길면: -1 반환
    v1=[a[0]-wbase[0],a[1]-wbase[1]]
    v2=[b[0]-wbase[0],b[1]-wbase[1]]
    if (v1[0]*v2[1])-(v1[1]*v2[0])>0:
        return 1
    elif (v1[0]*v2[1])-(v1[1]*v2[0])<0:
        return -1
    else:
        if (v1[0]**2+v1[1]**2)>(v2[0]**2+v2[1]**2):
            return -1
        else:
            return 1

def ccw(a,b,c,d): #벡터 a-b, c-d의 외적 ccw:1 cw:-1 line:0
    v1=[b[0]-a[0],b[1]-a[1]]
    v2=[d[0]-c[0],d[1]-c[1]]
    return (v1[0]*v2[1])-(v1[1]*v2[0])

def intersect(a,b): #a: ((ax1,ay1),(ax2,ay2)) , b ((bx1,by1),(bx2,by2))선분 교차하는지 판단 a,b가 점일때도 가능
    ap1=a[0]
    ap2=a[1]
    bp1=b[0]
    bp2=b[1]
    accw=ccw(ap1,ap2,ap1,bp1)*ccw(ap1,ap2,ap1,bp2)
    bccw=ccw(bp1,bp2,bp1,ap1)*ccw(bp1,bp2,bp1,ap2)
    if accw==0 and bccw==0:
        if ap1 == ap2: #a가 점일떄
            if min(bp1[0],bp2[0]) <= ap1[0] <= max(bp1[0],bp2[0]) and min(bp1[1],bp2[1]) <= ap1[1] <= max(bp1[1],bp2[1]):
                return 1
            return 0
        if bp1 == bp2: #b가 점일때
            if min(ap1[0],ap2[0]) <= bp1[0] <= max(ap1[0],ap2[0]) and min(ap1[1],ap2[1]) <= bp1[1] <= max(ap1[1],ap2[1]):
                return 1
            return 0
        if min(ap1[0],ap2[0])<max(ap1[0],ap2[0])<min(bp1[0],bp2[0])<max(bp1[0],bp2[0]):
            return 0
        if min(ap1[1],ap2[1])<max(ap1[1],ap2[1])<min(bp1[1],bp2[1])<max(bp1[1],bp2[1]):
            return 0
        if min(bp1[0],bp2[0])<max(bp1[0],bp2[0])<min(ap1[0],ap2[0])<max(ap1[0],ap2[0]):
            return 0
        if min(bp1[1],bp2[1])<max(bp1[1],bp2[1])<min(ap1[1],ap2[1])<max(ap1[1],ap2[1]):
            return 0
        return 1
    elif accw==0 or bccw==0:
        if accw>0 or bccw>0:
            return 0
        return 1
    elif accw<0 and bccw<0:
        return 1
    return 0

def inside(point, convex): #point가 convex 내부인지 판단
    for i in range(len(convex)):
        if ccw(point, convex[i-1], point, convex[i]) <= 0:
            return 0
    return 1
        
N=int(sys.stdin.readline().rstrip())

for _ in range(N):
    n, m =map(int,sys.stdin.readline().rstrip().split())

    black = []
    white = []
    
    for _ in range(n):
        x, y = map(int,sys.stdin.readline().rstrip().split())
        black.append((x,y))

    for _ in range(m):
        x, y = map(int,sys.stdin.readline().rstrip().split())
        white.append((x,y))

    if n == 0 or m == 0:
        print('YES')
        continue

    black= sorted(black,key=lambda x:(x[1],x[0]))
    white = sorted(white,key=lambda x:(x[1],x[0]))
    bbase = black[0][:]
    wbase = white[0][:]
    del black[0]
    del white[0]

    black = sorted(black, key = cmp_to_key(bcmpccw), reverse = True)
    white = sorted(white, key = cmp_to_key(wcmpccw), reverse = True)

    bconvex = []
    wconvex = []
    bconvex.append(bbase)
    wconvex.append(wbase)
    if black:
        bconvex.append(black[0])
        if n >= 3:
            for i in range(1,n-1):
                new=black[i]
                if ccw(bconvex[-2],bconvex[-1],bconvex[-1],new)>0:
                    bconvex.append(new)
                    
                elif ccw(bconvex[-2],bconvex[-1],bconvex[-1],new)<0:
                    bconvex.pop()
                    while ccw(bconvex[-2],bconvex[-1],bconvex[-1],new)<=0:
                        bconvex.pop()
                    bconvex.append(new)
                    
                elif ccw(bconvex[-2],bconvex[-1],bconvex[-1],new)==0:
                    bconvex.pop()
                    bconvex.append(new)

    if white:
        wconvex.append(white[0])
        if m >= 3:
            for i in range(1,m-1):
                new=white[i]
                if ccw(wconvex[-2],wconvex[-1],wconvex[-1],new)>0:
                    wconvex.append(new)
                    
                elif ccw(wconvex[-2],wconvex[-1],wconvex[-1],new)<0:
                    wconvex.pop()
                    while ccw(wconvex[-2],wconvex[-1],wconvex[-1],new)<=0:
                        wconvex.pop()
                    wconvex.append(new)
                    
                elif ccw(wconvex[-2],wconvex[-1],wconvex[-1],new)==0:
                    wconvex.pop()
                    wconvex.append(new)

    ans = 0
    
    if len(bconvex) < 3 and len(wconvex) < 3: #convex가 안만들어짐
        for b in range(len(bconvex)):
            for w in range(len(wconvex)):
                if wconvex[w-1] == wconvex[w] and bconvex[b-1] == bconvex[b]:
                    continue
                if intersect((bconvex[b-1],bconvex[b]), (wconvex[w-1], wconvex[w])):
                    ans = 1
                    break
     
    else:
        for b in range(len(bconvex)):
            for w in range(len(wconvex)):
                if intersect((bconvex[b-1],bconvex[b]), (wconvex[w-1], wconvex[w])):
                    ans = 1
                    break

        if inside(wconvex[0], bconvex) == 1:
            ans = 1
        if inside(bconvex[0], wconvex) == 1:
            ans = 1
    
    if ans == 1:
        print('NO')
    else:
        print('YES')