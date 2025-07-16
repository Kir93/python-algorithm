def solution(name, yearning, photo):
    answer = []
    point_dict = dict(zip(name,yearning))
    
    for ph in photo:
        s = 0
        
        for p in ph:
            if p in point_dict:
                s += point_dict[p]
                
        answer.append(s)
                
    return answer