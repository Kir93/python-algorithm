# 가까운 수
def solution(array, n):
    box = []
    array.sort()
    for x in array:
        box.append(abs(n-x))
    return array[box.index(min(box))]

# retry
def solution(array, n):
    array.sort()
    answer = []
    for i in array:
        answer.append(abs(n-i))
    return array[answer.index(min(answer))]