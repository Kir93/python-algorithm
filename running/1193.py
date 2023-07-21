x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

a = line - x + 1
b = x

if line%2 == 0:
    a = x
    b = line - x + 1

print(f'{a}/{b}')