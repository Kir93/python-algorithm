# 저주의 숫자 3
def solution(n):
    answer = 0
    
    for i in range(0, n):
        while answer % 3 == 0 or "3" in str(answer):
            answer += 1
        answer += 1

    return answer - 1

# retry
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer%3 == 0 or '3' in str(answer):
            answer += 1
            
    return answer