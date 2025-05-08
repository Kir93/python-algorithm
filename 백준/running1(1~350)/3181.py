g = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
n = input().split(' ')
r = ''
for i in range(len(n)):
    if i == 0: r += n[i][0].upper()
    elif n[i] not in g: r += n[i][0].upper()
print(r)