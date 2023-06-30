r = 0
n = int(input())
lenN = len(str(n))
for i in range(lenN - 1):
    r += 9 * 10 ** i * (i + 1)
print(r + (n - 10 ** (lenN - 1) + 1) * lenN)