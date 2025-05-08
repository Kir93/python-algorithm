import sys 
input = sys.stdin.readline

def isSamePoint(d,x,y,X,Y):
    if Y == d*(X-x) +y:
        return True
    else:
        return False

def findPoint(d1,d2,x1,y1,x3,y3):
    X = (y3-y1+x1*d1-x3*d2)/(d1-d2)
    Y = d1*(X-x1)+y1
    return (X,Y)

def findPointInf(d,X,x,y):
    Y = d*(X-x)+y
    return (X,Y)
n = int(input())

for _ in range(n):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int, input().split())
    
    if x1 != x2 and x3 != x4:
        d1 = (y1-y2)/(x1-x2)
        d2 = (y3-y4)/(x3-x4)
        if d1 == d2:
            if isSamePoint(d1,x1,y1,x3,y3):
                print("LINE")
                
            else:
                print("NONE")
        
        else:
            point = findPoint(d1,d2,x1,y1,x3,y3)
            print("POINT {:.2f} {:.2f}".format(point[0],point[1]))
    
    else:
        if x1 == x2 and x3 == x4:
            if x1==x3:
                print("LINE")
            else:
                print("NONE")
        else:
            if  x1 == x2 :
                d2 = (y3-y4)/(x3-x4)
                
                point = findPointInf(d2,x1,x3,y3)
                print("POINT {:.2f} {:.2f}".format(point[0],point[1]))
            elif  x3 == x4 :
                d1 = (y1-y2)/(x1-x2)
                
                point = findPointInf(d1,x3,x1,y1)
                print("POINT {:.2f} {:.2f}".format(point[0],point[1]))