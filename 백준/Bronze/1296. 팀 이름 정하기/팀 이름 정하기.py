y = input()
n = int(input())
ls = sorted([input() for _ in range(n)])
max_p = max_i = 0

for i in range(n):
    L = y.count('L') + ls[i].count('L')
    O = y.count('O') + ls[i].count('O')
    V = y.count('V') + ls[i].count('V')
    E = y.count('E') + ls[i].count('E')

    r = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if max_p < r:
        max_p = r
        max_i = i

print(ls[max_i])