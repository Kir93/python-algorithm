t = [i * (i + 1) // 2 for i in range(1, 46)]
e = [0] * 1001

for i in t:
    for j in t:
        for k in t:
            num = i + j + k
            if num <= 1000: e[num] = 1

for _ in range(int(input())): print(e[int(input())])