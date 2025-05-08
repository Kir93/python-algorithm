# 최빈값 구하기
def solution(array):
    answer = dict()
    for x in array:
        answer[x] = answer.get(x, 0) + 1
    r = [0, 0]
    temp = [0, 0]
    for x in answer.items():
        if x[1] > r[1] and x[1] > temp[1]:
            r = [x[0], x[1]]
            temp = [0, 0]
        elif x[1] == r[1]:
            temp = [x[0], x[1]]
    return r[0] if temp[1] == 0 else -1

# Best solution
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1

# Best solution2
def solution(array):
    idx = [0] * 1001
    for i in array:
        idx[i] +=1
    if idx.count(max(idx)) >1:
        return -1
    return idx.index(max(idx))