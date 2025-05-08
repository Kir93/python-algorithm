tt = int(input())
for t in range(tt):
    n = int(input())
    for i in range(n):
        if i == 0: print('#'*n)
        elif i + 1 == n: print('#'*n)
        else:
            for j in range(n):
                if j == 0: print('#', end='')
                elif j + 1 == n: print('#')
                else: print('J', end='')
    if t + 1 < tt:print()