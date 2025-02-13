# 대문자와 소문자
def solution(my_string):
    return ''.join(x.upper() if x.islower() else x.lower() for x in my_string)

# Best Solution
def solution(my_string):
    return my_string.swapcase()

# swapcase()는 대문자는 소문자로, 소문자는 대문자로 바꿔주는 함수이다.