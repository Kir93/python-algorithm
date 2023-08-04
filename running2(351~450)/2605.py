n = int(input())
ls = list(map(int, input().split()))
r = []
for i in range(n):
    r.insert(ls[i], i+1)
print(*r[::-1])