# 문자열 바꿔서 찾기
def solution(myString, pat):
    answer = ''
    for x in myString:
        if x == 'A': answer += 'B'
        else: answer += 'A'
    return bool(answer.find(pat))

# Best solution
def solution(myString, pat):
    return int(''.join('A' if x == 'B' else 'B' for x in pat) in myString)