def isPrime(num):
    if num <= 1: return False
    else:
        for i in range(2, int((num**0.5))+1):
            if num%i == 0: return False
        return True
while True:
    n = int(input())
    if n == 0: exit()
    else:
        for i in range(n-1, 2, -1):
            x = y = 0
            if isPrime(i):
                x = i
                if isPrime(n-x):
                    print(f'{n} = {n-x} + {x}')
                    break