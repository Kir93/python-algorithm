T = int(input())
A, B, C, D, E = map(int, input().split())
res = 0

for i in [A, B, C, D, E]:
    if i == T: res += 1
    
print(res)