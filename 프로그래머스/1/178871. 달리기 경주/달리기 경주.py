def solution(players, callings):
    rank = {player: idx for idx, player in enumerate(players)}
    for call in callings:
        idx = rank[call]
        if idx > 0:
            players[idx], players[idx - 1] = players[idx - 1], players[idx]
            rank[players[idx]] = idx
            rank[players[idx - 1]] = idx - 1
    return players