def solution(friends, gifts):
    friends_len = len(friends)
    friend_idx = {name: i for i, name in enumerate(friends)}
    ls = [[0] * friends_len for _ in range(friends_len)]
    
    next_month_gift = dict()
    gift_score = dict()
    
    # 선물 지수와 다음 달 받을 선물 초기화
    for friend in friends:
        next_month_gift[friend] = 0
        gift_score[friend] = 0
        
    
    # 선물 배열을 통해 주고 받은 선물 2차원 배열에 저장
    # 선물 지수 값 계산(선물 주면 +1, 받으면 -1)
    for gift in gifts:
        giver, receiver = gift.split()
        
        ls[friend_idx[giver]][friend_idx[receiver]] += 1
        gift_score[giver] += 1
        gift_score[receiver] -= 1
    
    for i in range(friends_len):
        for j in range(i + 1, friends_len):
            f1, f2 = friends[i], friends[j]
            g1, g2 = ls[i][j], ls[j][i]
            
            # 내가 상대방 보다 선물 많이 줬으면 다음 달 선물 +1
            if g1 > g2:
                next_month_gift[f1] += 1
            # 상대방이 나 보다 선물 많이 줬으면 상대방 다음 달 선물 +1
            elif g1 < g2:
                next_month_gift[f2] += 1
            # 서로 같다면
            else:
                gi, gj = gift_score[f1], gift_score[f2]
                
                # 선물 지수가 내가 높다면 내 다음 달 선물 +1
                if gi > gj:
                    next_month_gift[f1] += 1
                # 선물 지수가 상대가 높다면 상대방 다음 달 선물 +1
                elif gi < gj:
                    next_month_gift[f2] += 1
            
    return max(next_month_gift.values())