# 안전지대 - retry
def solution(board):
    answer = 0
    n = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    boom = []
    
    # 폭탄 위치 저장
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: boom.append((i, j))
    
    # 폭탄 주변 8방향에 1로 표시
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주변의 범위를 벗어나지 않았을 때 
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1
    
    # 안전지대 개수 세기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0: answer += 1
    
    return answer