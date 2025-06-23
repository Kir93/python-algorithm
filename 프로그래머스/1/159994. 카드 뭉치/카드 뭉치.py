def solution(cards1, cards2, goal):
    cards1_index = cards2_index = 0
    for card in goal:
        if cards1_index < len(cards1) and cards1[cards1_index] == card:
            cards1_index += 1
        elif cards2_index < len(cards2) and cards2[cards2_index] == card:
            cards2_index += 1
        else:
            return 'No'
    return 'Yes'