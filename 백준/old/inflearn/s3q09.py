import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp)==0:
        break;
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt=lt+1
        else:
            rt=rt-1
    tmp.clear()

print(len(res))
print(res)

#new mycode
import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
data = list(map(int, input().split()))
res = ''
r = 0
lt = 0
rt = n-1
while lt <= rt:
    if data[lt] < r or data[rt] < r:
        if data[lt] < r and data[rt] < r:
            break
        elif data[lt] < r and data[rt] > r:
            res += 'R'
            r = data[rt]
            rt -= 1
        elif data[rt] < r and data[lt] > r:
            res += 'L'
            r = data[lt]
            lt += 1
    if data[lt] > r and data[lt] < data[rt]:
        res += 'L'
        r = data[lt]
        lt += 1
    if data[rt] > r and data[rt] < data[lt]:
        res += 'R'
        r = data[rt]
        rt -= 1
print(len(res))
print(res)
