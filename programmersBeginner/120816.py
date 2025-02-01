# 피자 나눠 먹기 (3)
def solution(slice, n):
    return n//slice + bool(n%slice)

# Best solution1
def solution(slice, n):
    return (n+slice-1)//slice

# Best solution2
def solution(slice, n):
    return (n-1)//slice + 1

# 올림을 구하는 공식
# 1. (n + slice - 1) // slice
# 2. (n - 1) // slice + 1