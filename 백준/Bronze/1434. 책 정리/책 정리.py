n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0

while True:
    if a[i] >= b[j]:
        a[i] -= b[j]
        j += 1
    elif a[i] < b[j]:
        i += 1
    if i == n or j == m:
        break

print(sum(a))