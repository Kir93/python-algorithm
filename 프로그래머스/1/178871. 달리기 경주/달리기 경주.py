def solution(players, callings):
    player_number = {player: i for i, player in enumerate(players)}
    
    for player in callings:
        i = player_number[player]
        if i == 0:
            continue

        front = players[i - 1]
        players[i], players[i - 1] = front, player
        player_number[player], player_number[front] = i - 1, i

    return players