def divisor(n):
    c = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n%i == 0:
            c += 1
            if i ** 2 != n: c += 1
    return c

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if divisor(i)%2 == 0: answer += i
        else: answer -= i 
    return answer