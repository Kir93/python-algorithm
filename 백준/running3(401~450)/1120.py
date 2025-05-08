a, b = input().split()
r = []
for i in range(len(b)-len(a)+1):
    c = 0
    for j in range(len(a)):
        if a[j] != b[i+j]: c += 1
    r.append(c)
print(min(r))