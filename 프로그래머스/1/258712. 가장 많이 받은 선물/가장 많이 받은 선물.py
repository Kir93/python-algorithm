def solution(friends, gifts):
    fl = len(friends)
    ls = [[0 for _ in range(fl)] for _ in range(fl)]
    ns = dict()
    gs = dict()
    
    # 선물 지수화 다음 달 받을 선물 초기화
    for f in friends:
        ns[f] = 0
        gs[f] = 0
    
    # 선물 배열을 통해 주고 받은 선물 2차원 배열에 저장
    # 선물 지수 값 계산(선물 주면 +1, 받으면 -1)
    for gift in gifts:
        s, r = gift.split()
        ls[friends.index(s)][friends.index(r)] += 1
        gs[s] += 1
        gs[r] -= 1
    
    for i in range(fl):
        for j in range(i, fl):
            # 주고 받은 사람 나 면 제외
            if i == j: continue
            # 내가 상대방 보다 선물 많이 줬으면 다음 달 선물 +1
            if ls[i][j] > ls[j][i]:
                ns[friends[i]] += 1
            # 상대방이 나 보다 선물 많이 줬으면 상대방 다음 달 선물 +1
            elif ls[i][j] < ls[j][i]:
                ns[friends[j]] += 1
            # 서로 같다면
            else:
                gi = gs[friends[i]]
                gj = gs[friends[j]]
                # 선물 지수가 내가 높다면 내 다음 달 선물 +1
                if gi > gj:
                    ns[friends[i]] += 1
                # 선물 지수가 상대가 높다면 상대방 다음 달 선물 +1
                elif gi < gj:
                    ns[friends[j]] += 1
            
    return max(ns.values())