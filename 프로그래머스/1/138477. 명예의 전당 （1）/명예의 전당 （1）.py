def solution(k, score):
    answer = []
    honer_list = []
    for i in range(len(score)):
        if len(honer_list) == k and score[i] > min(honer_list):
            honer_list.pop(honer_list.index(min(honer_list)))
        if len(honer_list) != k:
            honer_list.append(score[i])
            
        answer.append(min(honer_list))
            
    return answer