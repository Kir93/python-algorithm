# 문자열 섞기
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer

# Best solution
def solution(str1, str2):
    return ''.join(s1 + s2 for s1, s2 in zip(str1,str2))