import sys
input = sys.stdin.readline

def ccw(a,b,c,d,e,f):
    return (a*d+c*f+e*b) - (c*b+e*d+a*f)

x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())
if ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<0:
    print(1)
else:
    print(0)