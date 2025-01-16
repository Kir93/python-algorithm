# 글자 지우기
def solution(my_string, indices):
    answer = list(my_string)
    for i in indices:
        my_string[i] = '_'
    return ''.join(answer).replace('_', '')

# Best solution 1
def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:answer+=my_string[i]
    return answer

# Best solution 2
def solution(my_string, indices):
    for idx in indices:
        my_string = my_string[:idx] + 'X' + my_string[idx+1:]
    return my_string.replace('X', '')

print(solution("apporoograpemmemprs",[1, 16, 6, 15, 0, 10, 11, 3]))