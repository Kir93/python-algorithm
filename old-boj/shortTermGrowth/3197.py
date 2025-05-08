from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ICE = 2
SWAN = 1
WATER = 0

r,c = map(int, input().split())
board = []
visited = [[False] * c for _ in range(r)]
ice_visited = [[0] * c for _ in range(r)]
visited_num = 1

edges = deque()
swan = []

for x in range(r):
    board.append(list(input().strip()))
    for y in range(c):
        if board[x][y] == '.':
            board[x][y] = WATER
        elif board[x][y] == 'L':
            swan = (x,y)
            board[x][y] = SWAN
        else:
            board[x][y] = ICE

def solv():
    global visited, visited_num
    ans = 0
    set_edges()
    visited[swan[0]][swan[1]] = True
    swan_q = deque([swan])
    while True:
        visited_num += 1
        swan_q = swan_bfs(swan_q)
        if not swan_q:
            print(ans)
            break
        melt_ice()
        ans += 1

def melt_ice():
    global edges,ice_visited,remove_visited

    edges_cnt = len(edges)
    for _ in range(edges_cnt):
        x,y = edges.pop()
        board[x][y] = WATER
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny):
                if board[nx][ny] == ICE and ice_visited[nx][ny] == 0:
                    edges.appendleft((nx,ny))
                    ice_visited[nx][ny] = visited_num

def swan_bfs(swan_q):
    global visited

    nxt_q = deque()
    while swan_q:
        x,y = swan_q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == SWAN:
                    return None
                elif board[nx][ny] == ICE:
                    nxt_q.appendleft((nx,ny))
                else:
                    swan_q.appendleft((nx,ny))
    return nxt_q
def set_edges():
    for x in range(r):
        for y in range(c):
            if board[x][y] == ICE:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if point_validator(nx, ny) and board[nx][ny] in [WATER, SWAN]:
                        ice_visited[x][y] = visited_num
                        edges.appendleft((x, y))
                        break

def point_validator(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True

solv()