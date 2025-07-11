def solution(k, score):
    answer = []
    honer_list = []
    for s in score:
        if len(honer_list) == k:
            min_score = min(honer_list)
            if s > min_score:
                honer_list.remove(min_score)
                honer_list.append(s)
        else:
            honer_list.append(s)
            
        answer.append(min(honer_list))
            
    return answer