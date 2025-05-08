# 2557
print('Hello World')

# 1000
a, b = map(int, input().split())
print(a+b)

# 2558
a = int(input())
b = int(input())
print(a+b)

# 10950
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a+b)

# 10951
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# 10952
while True:
    try:
        a, b = map(int, input().split())
        if a==b==0: break
        print(a+b)
    except:
        break

# 10953
t = int(input())

for _ in range(t):
    a, b = map(int, input().split(','))
    print(a+b)

# 11021
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')

# 11022
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')