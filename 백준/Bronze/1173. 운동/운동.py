N, m, M, T, R = map(int, input().split())
firstM = m
time = 0

while N > 0:
    if time == 0 and m + T > M:
        time = -1
        break
    if m + T <= M:
        m += T
        N -= 1
    elif m + T > M:
        if m - R < firstM:
            m = firstM
        else:
            m -= R
    time += 1

print(time)
