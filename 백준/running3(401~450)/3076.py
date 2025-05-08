r, c = map(int, input().split())
a, b = map(int, input().split())

ls = []
t1, t2 = '', ''

for i in range(c):
    if i % 2: 
        t1 += '.'*b
        t2 += 'X'*b
    else:
        t1 += 'X'*b
        t2 += '.'*b
        
for i in range(r):
    if i%2:
        for _ in range(a): print(t2)
    else:
        for _ in range(a): print(t1)