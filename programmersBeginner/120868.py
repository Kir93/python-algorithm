# 삼각형의 완성조건 (2) - retry
def solution(sides):
    answer = 0
    maxSide = max(sides)
    minSide = min(sides)
    
    # sides에 있는 변(maxSides)이 가장 길 경우
    for _ in range (maxSide - minSide + 1, maxSide + 1):
        answer += 1
        
    # 새로운 변(new_side)가 가장 길 경우
    for _ in range (maxSide + 1, maxSide + minSide):
        answer += 1
        
    return answer

# Best Solution 1
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1

# Best Solution 2
def solution(sides):
    return 2 * min(sides) - 1