n = int(input())
li = list(map(int, input().split()))
a = 0
re = []

for i in range(n-1):
    if li[i] < li[i+1]: a += li[i+1] - li[i]
    else:
        re.append(a)
        a = 0
        
re.append(a)
print(max(re))