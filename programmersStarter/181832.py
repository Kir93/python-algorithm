# 정수를 나선형으로 배치하기 - retry
def solution(n):
    if n == 1: return [[1]]

    answer = [[0] * n for _ in range(n)]
    x = y = 0
    dir = 'r'
    
    for i in range(n**2):
        answer[y][x] = i + 1
        if dir == 'r':
            x += 1
            if x == n-1 or answer[y][x+1] != 0: dir = 'b'
        elif dir == 'b':
            y += 1
            if y == n-1 or answer[y+1][x] != 0: dir = 'l'
        elif dir == 'l':
            x -= 1
            if x == 0 or answer[y][x-1] != 0: dir = 't'
        elif dir == 't':
            y -= 1
            if y == 1 or answer[y-1][x] != 0: dir = 'r'
            
    return answer
