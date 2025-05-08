def is_prime(value) :
    if value > max_value :
        for prime in primes :
            if prime >= value :
                break
            elif value % prime == 0 :
                return False

        return True
    else :
        return data[value]

max_value = 2000000
data = [False, False] + [True for _ in range(max_value-1)]
primes = []
for i in range(2, max_value + 1) :
    if data[i] :
        primes.append(i)
        for j in range(i+i, max_value, i) :
            data[j] = False

t = int(input())
for _ in range(t) :
    a, b = map(int, input().split())
    sum_value = a + b

    if sum_value < 4 :
        print('NO')
    elif sum_value % 2 == 0 :
        print('YES')
    else :
        if is_prime(sum_value - 2) :
            print('YES')
        else :
            print('NO')