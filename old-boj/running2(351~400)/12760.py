n,m=map(int, input().split())
player=[]
answer=[0]*n
result=[]
for i in range(n):
    tmp=sorted(list(map(int, input().split())))
    player.append(tmp)
for i in range(m):
    tmp=[]
    for j in range(n):
        tmp.append(player[j][i])
    mx=max(tmp)
    for j in range(n):
        if mx==tmp[j]:
            answer[j]+=1
winner=max(answer)
for i in range(n):
    if answer[i]==winner:
        result.append(i+1)
print(*result)