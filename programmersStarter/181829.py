# 이차원 배열 대각선 순회하기 - retry
def solution(board, k):
    answer = 0
    for i in range(min(k+1, len(board))):
        for j in range(min(k-i+1, len(board[i]))):
            answer += board[i][j]
    return answer

# Best solution
def solution(board, k):
    return sum(
        board[i][j]
        for i in range(min(k+1, len(board)))
        for j in range(min(k-i+1, len(board[i])))
        )
