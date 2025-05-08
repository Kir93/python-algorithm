import sys
input=sys.stdin.readline

m=int(input())
n=int(input())

graph=[list(map(int,input().split())) for _ in range(8)]
a=[0]*8
b=[0]*8

for i in range(8):
    now=0
    for j in range(8):
        now+=graph[i][j]-m
    a[i]=now

for i in range(8):
    now=0
    for j in range(8):
        now+=graph[j][i]-m
    b[i]=now

s=sum(a)

for i in range(8):
    for j in range(8):
        now=(15*(a[i]+b[j])-2*s-105*(graph[i][j]-m))//105
        if now==0: print(".",end=' ')
        elif now==1: print("+", end=' ')
        else: print("-",end=' ')
    print()
