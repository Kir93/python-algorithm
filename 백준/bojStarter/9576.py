t = int(input())
for _ in range(t) :
    n, m = map(int, input().split())
    flag = [False] * (n + 1)

    data = []
    for _ in range(m) :
        a, b = map(int, input().split())
        data.append((a, b))

    data.sort(key=lambda x: x[1])

    result = 0
    while data :
        a, b = data.pop(0)
        for i in range(a, b + 1) :
            if not flag[i] :
                flag[i] = True
                result += 1
                break

    print(result)