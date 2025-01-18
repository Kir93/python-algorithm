# 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    return answer

solution("He11oWor1d","lloWorl", 2)
# solution("Program29b8UYP","merS123", 7)