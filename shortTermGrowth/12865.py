
n, k = map(int, input().split())

result = {0:0}

for _ in range(n):
    w, v = map(int, input().split())
    cache = {}
    for saveW, saveV in result.items():
        newW = saveW + w
        newV = saveV + v
        if newW <= k and newV > result.get(newW, 0):
            cache[newW] = newV
    result.update(cache)
print(max(result.values()))
