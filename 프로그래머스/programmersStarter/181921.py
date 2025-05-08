# 배열 만들기 2 - 다시 풀기
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if not set(str(i)) - set(['0', '5']):
            answer.append(i)
    return answer if answer else [-1]