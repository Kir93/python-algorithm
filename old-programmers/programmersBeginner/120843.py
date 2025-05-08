# 공 던지기
def solution(numbers, k):
    answer = 0
    for _ in range(k-1):
        answer += 2
        if answer > len(numbers):
            answer -= len(numbers)
    return numbers[answer]

# Best solution
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]