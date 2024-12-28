import sys
from collections import deque
T = int(input())

for _ in range(T):
    A, B = map(int,sys.stdin.readline().rstrip().split())

    visited = [False for i in range(10001)]
    deq = deque()
    deq.append([A,''])
    visited[A] = True

    while deq:
        num, command = deq.popleft()

        if num == B:
            print(command)
            break

        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            deq.append([d, command + 'D'])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            deq.append([s, command + 'S'])

        l = num // 1000 + (num % 1000)*10
        if not visited[l]:
            visited[l] = True
            deq.append([l, command + 'L'])

        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            deq.append([r, command + 'R'])