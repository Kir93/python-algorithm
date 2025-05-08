sum = 0
pg = 0
gp = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}

for _ in range(20):
    n, c, g = map(str, input().split())
    c = float(c)
    if g != 'P':
        sum += c
        pg += gp[g] * c

print("{:.6f}".format(pg/sum,6)) 