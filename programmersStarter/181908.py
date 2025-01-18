# 접미사인지 확인하기
def solution(my_string, is_suffix):
    answer = 0
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            answer = 1
            break
    return answer

# Best Solution 1
def solution(my_string, is_suffix):
    return int(my_string[-len(is_suffix):] == is_suffix)

# Best Solution 2
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))