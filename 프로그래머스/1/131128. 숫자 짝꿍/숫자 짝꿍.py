def solution(X, Y):
    answer = []
    
    count_x = [0] * 10
    count_y = [0] * 10
    
    for x in X:
        count_x[int(x)] += 1
    for y in Y:
        count_y[int(y)] += 1
        
    for i in range(9, -1, -1):
        min_num = min(count_x[i], count_y[i])
        answer.append(str(i) * min_num)
            
    r = ''.join(answer)

    if not r:
        return '-1'
    
    if r[0] == '0':
        return '0'
    
    return r