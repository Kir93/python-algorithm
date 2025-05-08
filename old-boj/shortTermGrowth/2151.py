from collections import deque

N = int(input())

listMap = []
listPos = []
visited = [[1000] * N for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(N):
    listMap.append(list(map(lambda x:x, input())))

for i in range(N):
    for j in range(N):
        if listMap[i][j] == '#':
            listPos.append((i,j))

startPosX, startPosY, endPosX, endPosY = listPos[0][0], listPos[0][1], listPos[1][0], listPos[1][1]
q = deque()
q.append((listPos[0], 0, 0))
q.append((listPos[0], 0, 1))
q.append((listPos[0], 0, 2))
q.append((listPos[0], 0, 3))

while q:
    (posX, posY), mirrorCount, direction = q.popleft()
    
    movePosX = posX+dx[direction]
    movePosY = posY+dy[direction]
        
    while 0 <= movePosX < N and 0<= movePosY < N and listMap[movePosX][movePosY] != '*':
        if listMap[movePosX][movePosY] == "!":
            if direction == 0 or direction == 2:
                q.append(((movePosX,movePosY), mirrorCount+1, 1))
                q.append(((movePosX,movePosY), mirrorCount+1, 3))
            else:
                q.append(((movePosX,movePosY), mirrorCount+1, 0))
                q.append(((movePosX,movePosY), mirrorCount+1, 2))

        if movePosX == endPosX and movePosY == endPosY:
            q.clear()
            break

        movePosX += dx[direction]
        movePosY += dy[direction]        

print(mirrorCount)