i, j = 0, 0

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

while i < n and j < m:
    if A[i] < B[j]:
        i += 1
    else:
        A[i] -= B[j]
        j += 1

print(sum(A))