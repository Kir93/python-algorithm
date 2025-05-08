#겹치는 선분의 길이
def solution(lines):
    # 1. 숫자선을 만들고, 색칠할 리스트 준비 (최대 범위 -100 ~ 100)
    lineMap = [0] * 201
    
    # 2. 선분을 숫자선에 맞게 색칠
    for start, end in lines:
        # -100을 0으로 맞추기 위해 +100
        for i in range(start + 100, end + 100):
            lineMap[i] += 1

    # 3. 2개 이상 겹친 부분의 길이 세기
    return sum(1 for i in lineMap if i >= 2)

# retry
def solution(lines):
    lineMap = [0] * 201
    
    for start, end in lines:
        for i in range(start+100, end+100):
            lineMap[i] += 1
    
    return sum(1 for i in lineMap if i > 1)