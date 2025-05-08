x, y = map(int, input().split())
ls = [x/y]
for _ in range(int(input())):
    xi, yi = map(int, input().split())
    ls.append(xi/yi)
print(f'{min(ls)*1000}')