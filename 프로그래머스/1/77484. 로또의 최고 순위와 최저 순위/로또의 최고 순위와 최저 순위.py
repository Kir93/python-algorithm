def solution(lottos, win_nums):
    win_check = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    unread_count = lottos.count(0)
    matched_count = len(set(lottos) & set(win_nums))

    return [win_check[unread_count + matched_count], win_check[matched_count]]