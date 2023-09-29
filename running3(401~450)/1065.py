r = 0
for i in range(1, int(input())+1):
    ls = list(map(int, str(i)))
    if i < 100: r += 1
    elif ls[0] - ls[1] == ls[1] - ls[2]: r += 1
print(r)