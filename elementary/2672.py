import sys
input = sys.stdin.readline

table = [list(map(int,input().split())) for _ in range(6)]

number = [i for i in range(7)]

go = ((-1 , 0) , (1 , 0) , (0 , -1) , (0 , 1))

def DFS(x , y , dx , dy , cnt):
    global save
    if cnt == 2:
        save.append(table[x][y])
    else:
        for i, j in go:
            X = x + i
            Y = y + j
            if 0 <= X < 6 and 0 <= Y < 6 and table[X][Y] != 0 and visited[X][Y] == False:
                visited[X][Y] = True
                if i == dx and j == dy:
                    DFS(X,Y,dx,dy,cnt+1)
                else:
                    DFS(X,Y,dx,dy,cnt)






stat = False
for x in range(6):
    for y in range(6):
        if table[x][y] == 0 or number[table[x][y]] != table[x][y]: continue
        save = []
        visited = [[False] * 6 for _ in range(6)]
        visited[x][y] = True
        for i , j in go:
            X = x + i
            Y = y + j
            if 0 <= X < 6 and 0 <= Y < 6 and table[X][Y] != 0:
                visited[X][Y] = True
                DFS(X,Y,i,j,1)
                if len(save) >= 2:
                    stat = True
                    break

        if number[save[0]] != save[0]:
            stat = True
            # print(x , y ,number[save[0]] , save[0] , table[x][y])
            break
        else:
            number[save[0]] , number[table[x][y]] = number[table[x][y]] , number[save[0]]
        if stat: break

    if stat: break
if stat : print(0)
else: print(number[1])
