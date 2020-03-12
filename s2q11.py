#my code
import sys
sys.stdin=open("input.txt","rt")
data = [list(map(int,input().split())) for _ in range(7)]
cnt=0
for i in range(7):
  for j in range(3):
    s=0
    e=4
    while(s<e):
      if data[i][s+j] == data[i][e+j]:
        s+=1
        e-=1
        if s==2:
          cnt+=1
      elif data[s+j][i] == data[e+j][i]:
        s+=1
        e-=1
        if s==2:
          cnt+=1
      else:
        break
print(cnt)

#best code
import sys
sys.stdin=open("input.txt", "r")
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break;
        else:
            cnt+=1
        
print(cnt)

#회문의 길이가 가변적일 때 코드
import sys
sys.stdin=open("input.txt", "r")
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
len=5
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+len]
        if tmp==tmp[::-1]:
            cnt+=1
        #tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
        for k in range(len//2):
            if board[i+k][j]!=board[len-k+i-1][j]:
                break;
        else:
            cnt+=1
        
print(cnt)

#new mycode
import sys
#sys.stdin=open("input.txt","rt")
n = 7
data = [list(map(int, input().split())) for _ in range(n)]
tot = 0
for i in range(n):
  d1 = d2 = False
  for j in range(3):
    for x in range(5):
      if data[i][x+j] == data[i][4+j-x]:
        d1 = True
      else:
        d1 = False
        break
    for y in range(5):
      if data[y+j][i] == data[4+j-y][i]:
        d2 = True
      else: 
        d2 = False
        break
    if d1 == True:  tot +=1
    if d2 == True:  tot +=1
print(tot)    
