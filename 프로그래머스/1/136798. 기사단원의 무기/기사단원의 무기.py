import math

def get_divisor_count(n):
    c = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n%i == 0:
            if i * i == n: c += 1
            else: c += 2
    return c

def solution(number, limit, power):
    answer = 0
    numbers = [get_divisor_count(i) for i in range(1, number+1)]
    
    for n in numbers:
        answer += power if n > limit else n

    return answer