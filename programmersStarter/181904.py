# 세로 읽기
def solution(my_string, m, c):
    answer = ''
    i = 0
    for w in my_string:
        if i == c-1: answer += w
        if i == m-1: i = 0
        else: i += 1
    return answer

# Best solution
def solution(s, m, c):
    return s[c-1::m]

# 파이썬 배열의 경우 start:end:step 형태로 지정
# 위의 경우 c-1번째에서 시작해서 m번째 만큼 건너 뛰고
# end가 지정되지 않았기 때문에 끝까지 실행한다는 의미