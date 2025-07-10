def solution(friends, gifts):
    friends_len = len(friends)
    friends_idx = {name: idx for idx, name in enumerate(friends)}
    gift_list = [[0] * friends_len for _ in range(friends_len)]

    next_month_count = dict()
    gift_score = dict()
    
    # 초기화
    for friend in friends:
        next_month_count[friend] = 0
        gift_score[friend] = 0

    # 주고 받은 선물 배열에 저장
    # 선물을 주면 +1, 받으면 -1
    for gift in gifts:
        giver, receiver = gift.split()

        gift_list[friends_idx[giver]][friends_idx[receiver]] += 1
        
        gift_score[giver] += 1
        gift_score[receiver] -= 1

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            friend1, friend2 = friends[i], friends[j]
            gift1, gift2 = gift_list[i][j], gift_list[j][i]

            # friend1가 상대방 보다 선물 많이 줬으면 friend1 다음 달 선물 +1
            if gift1 > gift2:
                next_month_count[friend1] += 1
            # friend2가 상대방 보다 선물 많이 줬으면 friend2 다음 달 선물 +1
            elif gift1 < gift2:
                next_month_count[friend2] += 1
            # 서로 같다면
            else:
                score1, score2 = gift_score[friend1], gift_score[friend2]

                # friend1가 상대방 보다 선물 점수가 높으면 friend1 다음 달 선물 +1
                if score1 > score2:
                    next_month_count[friend1] += 1
                # friend2가 상대방 보다 선물 점수가 높으면 friend2 다음 달 선물 +1
                elif score1 < score2:
                    next_month_count[friend2] += 1

    return max(next_month_count.values())