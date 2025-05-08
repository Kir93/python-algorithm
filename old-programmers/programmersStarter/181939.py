# 더 크게 합치기
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))

# max 함수의 경우 문자열, 문자열이나 숫자, 숫자로 비교 가능