# 피자 나눠 먹기 (1)
def solution(n):
    from math import ceil
    return ceil(n/7)

# Best solution
def solution(n):
    return (n - 1) // 7 + 1

# Best solution2
def solution(n):
    return (n + 6) // 7