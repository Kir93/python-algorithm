def calc_distance(board):
    dis = 0
    for i in range(4):
        for j in range(4):
            dis += (board[i][j] // 4 != i) + (board[i][j] % 4 != j)
    return dis

def solve(board, left_move_count, route):
    distance = calc_distance(board)

    if distance == 0: return route
    if left_move_count < distance // 4: return None

    for row in range(4):
        for moves in range(1,4):
            board[row][0],board[row][1],board[row][2],board[row][3] = board[row][3],board[row][0],board[row][1],board[row][2]
            sol = solve(board, left_move_count-1, route+[(1, row+1, moves)])
            if sol: return sol
        board[row][0],board[row][1],board[row][2],board[row][3] = board[row][3],board[row][0],board[row][1],board[row][2]

    for col in range(4):
        for moves in range(1,4):
            board[0][col],board[1][col],board[2][col],board[3][col] = board[3][col],board[0][col],board[1][col],board[2][col]
            sol = solve(board, left_move_count-1, route+[(2, col+1, moves)])
            if sol: return sol
        board[0][col],board[1][col],board[2][col],board[3][col] = board[3][col],board[0][col],board[1][col],board[2][col]

    return None


board = [list(map(lambda x: int(x)-1, input().split())) for _ in range(4)]
max_move = 0

while 1:
    sol = solve(board, max_move, [])

    if sol:
        print(max_move)
        for route in sol: print(*route)
        break
    max_move += 1