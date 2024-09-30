from sys import stdin

N, C =  map(int, stdin.readline().split())
M = int(stdin.readline())
infos = []
for _ in range(M):
    s, r, box = map(int, stdin.readline().split())
    infos.append((s, r, box))
infos.sort(key=lambda x :  x[1])

capa = [C]*N
total = 0
for s, r, box in infos:
    _min = C
    for i in range(s, r):
        if _min > min(capa[i], box) :
            _min = min(capa[i], box)
    for i in range(s, r):
        capa[i] -= _min
    total += _min
    
print(total)