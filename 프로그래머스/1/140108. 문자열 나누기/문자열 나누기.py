def solution(s):
    answer = 0
    prev = ''
    x_count = 0
    diff_count = 0
    
    for x in s:
        if x_count == 0:
            prev = x
            answer += 1

        if prev == x:
            x_count += 1
        else:
            diff_count += 1
        
        if x_count == diff_count:
            x_count = 0
            diff_count = 0
            
    return answer