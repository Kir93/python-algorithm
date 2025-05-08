# 2차원으로 만들기
def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]

# retry
def solution(num_list, n):
    return [num_list[i:n + i] for i in range(0, len(num_list), n)]