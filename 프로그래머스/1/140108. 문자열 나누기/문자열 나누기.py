def solution(s):
    answer = len_x = len_diff = 0
    prev = ''
    
    for x in s:
        if len_x == 0:
            prev = x
            answer += 1
        
        if x == prev:
            len_x += 1
        else:
            len_diff += 1
        
        if len_x == len_diff:
            len_x = len_diff = 0
        
    return answer