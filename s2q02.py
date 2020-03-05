import sys
#sys.stdin=open("input.txt","rt")
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res*10 + int(x)
print(res)

cnt = 0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1

print(cnt)

#new mycode
import sys
sys.stdin = open('input.txt', 'rt')
n = input()
s = ""
tot = 0
for x in n:
    if ord(x) >= 48 and ord(x) <= 57:
        s += x
s = int(s)
for i in range(1, s+1):
    if s % i == 0:
        tot += 1
print(s)
print(tot)
