a, b, c = map(int, input().split())
price_table = {0:0, 1:a, 2:b*2, 3:c*3}
ls = [0] * 100
r = 0
for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e): ls[i] += 1
for t in ls:
    r += price_table[t]
print(r)