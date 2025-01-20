# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
def solution(myString, pat):
    return myString[:myString.rfind(pat) + len(pat)]

# rfind, rindex는 문자열의 끝점을 기준으로 찾아내는 메소드