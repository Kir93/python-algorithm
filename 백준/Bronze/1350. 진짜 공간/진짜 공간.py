N = int(input())
li = list(map(int, input().split()))
S = int(input())
cnt = N

for s in li:
    if s > S:
        cnt += (s-1)//S
    elif s == 0:
        cnt -= 1
print(S*cnt)