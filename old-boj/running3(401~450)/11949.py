n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]
for i in range(1, m+1):
    for j in range(1, len(ls)):
        if ls[j - 1] % i > ls[j]% i:
            ls[j - 1], ls[j] = ls[j], ls[j - 1]

for num in ls: print(num)