from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def get_dist(a1x,a1y,a2x,a2y,b1x,b1y,b2x,b2y):
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    path = [[(0, 0) for _ in range(M + 1)] for _ in range(N + 1)]
    visited[b1x][b1y]=True
    visited[b2x][b2y]=True
    dis1=bfs(a1x,a1y,a2x,a2y,visited,path)
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    cx,cy=a2x,a2y
    while True:
        visited[cx][cy]=True
        if cx==a1x and cy==a1y:
            break
        cx,cy=path[cx][cy]

    dis2=bfs(b1x,b1y,b2x,b2y,visited,path)

    return dis1,dis2

def bfs(sx,sy,ex,ey,visited,path):
    q=deque()

    q.append((sx,sy,0))
    visited[sx][sy]=True
    while q:
        x,y,cnt=q.popleft()
        if x==ex and y==ey:
            return cnt
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]

            if nx<0 or nx>N or ny<0 or ny>M:
                continue
            if visited[nx][ny]==True:
                continue

            q.append((nx,ny,cnt+1))
            visited[nx][ny]=True
            path[nx][ny]=(x,y)

    return 1e9


N,M=map(int,input().split())
a1x,a1y=map(int,input().split())
a2x,a2y=map(int,input().split())
b1x,b1y=map(int,input().split())
b2x,b2y=map(int,input().split())

r1,r2=get_dist(a1x,a1y,a2x,a2y,b1x,b1y,b2x,b2y)
dis1=r1+r2

r3,r4=get_dist(b1x,b1y,b2x,b2y,a1x,a1y,a2x,a2y)
dis2=r3+r4

ans=min(dis1,dis2)

if ans>=1e9:
    print("IMPOSSIBLE")
else:
    print(ans)