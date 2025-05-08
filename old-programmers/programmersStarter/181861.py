# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for i in arr:
        for _ in range(i):
            answer.append(i)
    return answer

# Best solution
def solution(arr):
    answer = []
    for num in arr:
        answer.extend([num] * num)
    return answer