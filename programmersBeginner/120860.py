# 직사각형 넓이 구하기
def solution(dots):
    w = max(dots)[0] - min(dots)[0]
    h = max(dots)[1] - min(dots)[1]
    return w*h

# 직사각형의 넓이는 최대 x 좌표 - 최소 x 좌표와 같고 최대 y 좌표 - 최소 y 좌표와 같다.