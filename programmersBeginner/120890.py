# 가까운 수 - retry
def solution(array, n):
    box = []
    array.sort()
    for x in array:
        box.append(abs(n-x))
    return array[box.index(min(box))]