#bestcode
import sys
sys.stdin=open("input.txt", "r")
max=0
res=0
n=int(input())
for i in range(n):
    tmp=input().split() 
    tmp.sort() 
    a, b, c=map(int, tmp)
    if a==b and b==c:
        money=10000+(a*1000);
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money > res:
        res=money

print(res)

#mycode
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
bmoney = 0
for i in range(n):
    data = list(map(int,input().split()))
    if data[0] == data[1] == data[2]:
        money = 10000+(data[0]*1000)
    elif data[0] == data[1]:
        money = 1000+(data[0] * 100)
    elif data[1] == data[2]:
        money = 1000 + (data[0] * 100)
    elif data[0] == data[2]:
        money = 1000 + (data[0] * 100)
    elif data[0]!=data[1] and data[0]!=data[2] and data[1]!=data[2]:
        if data[0]>=data[1] and data[0]>=data[2]:
            money = data[0] * 100
        elif data[1]>=data[0] and data[1]>=data[2]:
            money = data[1] * 100
        elif data[2]>=data[0] and data[2]>=data[1]:
            money = data[1] * 100
    if bmoney < money:
        bmoney = money


print(bmoney)
