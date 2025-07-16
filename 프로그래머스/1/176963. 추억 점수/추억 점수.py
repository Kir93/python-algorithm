def solution(name, yearning, photo):
    answer = []
    
    for ph in photo:
        s = 0
        
        for p in ph:
            if p in name:
                s += yearning[name.index(p)]
                
        answer.append(s)
                
    return answer