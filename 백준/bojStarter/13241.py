numbers = list(map(int, input().split()))
numbers.sort(reverse = True)

A, B = numbers[0], numbers[1]

while B != 0:
    A = A%B
    A,B = B,A
    
print((numbers[0] * numbers [1]) // A)