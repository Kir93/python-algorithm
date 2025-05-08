# 문자 개수 세기
def solution(my_string):
    answer = [0 for _ in range(52)]
    for x in my_string:
        if x.isupper():
            answer[ord(x)-65]+=1
        else:
            answer[ord(x)-71]+=1
    return answer

# Best solution
def solution(my_string):
    alphabet_list = 'abcdefghijklmnopqrstuvwxyz'.upper() + 'abcdefghijklmnopqrstuvwxyz'
    return list(my_string.count(alphabet) for alphabet in alphabet_list)

