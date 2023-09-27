a, b = 1, 0
for i in range(int(input())):
    a, b = (a + b)%10, a%10
print(a)