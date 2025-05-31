def gcd(n, m):
    while m > 0:
        n, m = m, n%m
    return n

def lcm(n, m):
    for i in range(max(n, m), (n*m)+1):
        if i%n == 0 and i%m == 0:
            return i
    
def solution(n, m):
    return [gcd(n, m), lcm(n, m)]