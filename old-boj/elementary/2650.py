import sys, math
input=sys.stdin.readline

n=int(input())//2

dots = []

def ccw ( a,b,c ):
    x1,y1 = a
    x2,y2 = b
    x3,y3 = c
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def clamp ( a0, a1, b0, b1):
    if a0>a1: a0,a1 = a1,a0
    if b0>b1: b0,b1 = b1,b0
    return a0<b0<a1<b1 or b0<a0<b1<a1

def cross (a,b) :
    a0 = ccw(a[0],a[1],b[0])
    a1 = ccw(a[0],a[1],b[1])
    b0 = ccw(b[0],b[1],a[0])
    b1 = ccw(b[0],b[1],a[1])
    
    if a0==0 and a1==0 and b0==0 and b1==0:
        return clamp(a[0],a[1],b[0],b[1])
    else: return a0*a1 < 0 or b0*b1 < 0
    

def dot (a,b):
    if a==1:
        return (b,52)
    elif a==2:
        return (b,0)
    elif a==3:
        return (0,52-b)
    else:
        return (52,52-b)

for _ in range(n):
    a,b,c,d=map(int,input().split())
    
    dots += [(dot(a,b),dot(c,d))]

ans=[0] * n

for i in range(n):
    for j in range(i+1,n):
        if cross(dots[i],dots[j]):
            ans[i]+=1
            ans[j]+=1
print(sum(ans)//2)
print(max(ans))