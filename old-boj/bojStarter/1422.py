import sys
input = sys.stdin.readline
k, n = map(int, input().split())


def do_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            a = int(arr[i] + arr[j])
            b = int(arr[j] + arr[i])
            if a < b:
                arr[i], arr[j] = arr[j], arr[i]


arr = [input().rstrip() for _ in range(k)]

MAX = str(max(map(int, arr)))

for _ in range(k, n):
    arr.append(MAX)

do_sort(arr)

print(''.join(arr))