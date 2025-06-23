def solution(cards1, cards2, goal):
    for card in goal:
        if len(cards1) and cards1[0] == card:
            cards1.pop(0)
        elif len(cards2) and cards2[0] == card:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'