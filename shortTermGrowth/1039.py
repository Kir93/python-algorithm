from collections import deque

n,k = input().strip().split()
size = len(n)
n,k = map(int, [n,k])

def solv():
    answer = 0
    visited = set()

    q = deque([(n,0)])
    while q:
        now,cnt = q.pop()
        if cnt == k:
            answer = max(answer, now)
            continue

        arr = list(map(int, str(now)))
        for i in range(size-1):
            for j in range(i+1,size):
                if i == 0 and arr[j] == 0: continue
                arr[i],arr[j] = arr[j],arr[i]
                num = list_to_int(arr)
                if num+cnt+1 not in visited:
                    q.appendleft((num,cnt+1))
                    visited.add(num+cnt+1)
                arr[i],arr[j] = arr[j],arr[i]
    print(answer if answer > 0 else -1)
def list_to_int(arr):
    result = 0
    for num in arr:
        result = result*10+num
    return result
solv()