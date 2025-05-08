r = 0
n = int(input())
ls = sorted(list(map(int, input().split())))

for i in range(n):
    r += (ls[i]*i) - (ls[i]*(n-1-i))

print(r*2)