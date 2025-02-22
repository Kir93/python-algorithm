# 평행 - retry
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots

    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    
    return 1 if answer1 or answer2 or answer3 else 0

# 두 선이 평행인지 확인하는 방법은 두 선의 기울기가 같은지 확인하는 것이다.
# 두 선의 기울기가 같다는 것은 두 선이 평행하다는 것이다.
# 두 선의 기울기는 (y1-y2)/(x1-x2) = (y3-y4)/(x3-x4)로 구할 수 있다.
# 이건 즉 (y1-y2)*(x3-x4) = (y3-y4)*(x1-x2) 이렇게 곱셈으로 표현할 수 있다.
# 곱셈이 나눗셈보다 연산 속도가 빠르고, ZeroDivisionError가 발생할 가능성이 없다.