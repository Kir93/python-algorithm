time = list(map(int, input().split(':')))
hour = [h for h in range(1, 13)]
min_sec = [m_s for m_s in range(60)]

r = 0

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                if time[i] in hour and time[j] in min_sec and time[k] in min_sec:
                    r += 1

print(r)