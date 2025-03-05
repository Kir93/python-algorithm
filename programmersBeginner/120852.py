# 소인수분해
def primeFactors(n):
    arr, d = [], 2
    while n > 1:
        if n%d == 0:
            arr.append(d)
            n //= d
        else: d += 1
    return sorted(list(set(arr)))
    
def solution(n):
    return primeFactors(n)

# retry
def solution(n):
    answer, d = [], 2
    while n > 1:
        if n%d == 0:
            answer.append(d)
            n //= d
        else: d += 1
    return sorted(set(answer))