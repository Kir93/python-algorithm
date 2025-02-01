# 그림 확대
def solution(picture, k):
    answer = []
    for i in picture:
        char = ""
        for j in i:
            char += j*k
        for _ in range(k):
            answer.append(char)
    return answer

# .과 x의 개수도 k배를 해야되고 줄의 개수도 k배를 해야된다.

# Best solution
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        answer += [picture[i].replace('.', '.' * k).replace('x', 'x' * k)] * k
    return answer

# retry
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        answer += [picture[i].replace('.', '.'*k).replace('x', 'x'*k)] * k
    return answer