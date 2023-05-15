gs = [1,2,3,3,4,10]
ss = [1,2,2,2,3,5,10]
for i in range(int(input())):
    g = list(map(int, input().split()))
    s = list(map(int, input().split()))
    gp = 0
    for j in range(len(g)): gp += g[j] * gs[j]
    for j in range(len(s)): gp -= s[j] * ss[j]
    winner = 'No victor on this battle field'
    if gp > 0:
        winner = 'Good triumphs over Evil'
    elif gp < 0:
        winner = 'Evil eradicates all trace of Good'
    print(f'Battle {i+1}: {winner}')