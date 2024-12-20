dance = {'ChongChong'}

for _ in range(int(input())):
    n, m = map(str, input().split())
    
    if n in dance: dance.add(m)
    if m in dance: dance.add(n)

print(len(dance))
