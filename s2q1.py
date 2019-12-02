import sys
sys.stdin=open("input.txt","rt")
n = int(input())
data = []
result = ["" for i in range(n)]
for i in range(n):
    data.append(input())

#my code
for i in range(n):
    for j in range(len(data[i])//2):
        if data[i][j].lower() != data[i][len(data[i])-1-j].lower():
            result[i] = "NO"
            break
        else:
            result[i] = "YES"

for idx, i in enumerate(result):
    print('#{} {}'.format(idx+1, i))
    
#best code
import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
for i in range(1, n+1):
    str=input()
    str=str.upper()
    for j in range(len(str)//2):
        if str[j]!=str[-1-j]:
            print("#%d NO" %i)
            break
    else:
        print("#%d YES" %i)

#best order code

import sys
sys.stdin=open("input.txt", "r")
n=int(input())
for i in range(n):
    str=input()
    str=str.upper()
    if str==str[::-1]:
        print("#%d YES" %i)
    else:
        print("#%d NO" %i)
