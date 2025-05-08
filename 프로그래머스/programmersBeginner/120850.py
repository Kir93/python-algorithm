# 문자열 정렬하기 (1)
def solution(my_string):
    return sorted([int(num) for num in my_string if num.isdigit()])

# num.isdigit()을 통해 문자인지 숫자인지 구분할 수 있다.