# 주사위 게임 2
def solution(a, b, c):
    answer = a + b + c
    if a == b or b == c or a == c: answer *= a**2 + b**2 + c**2
    if a == b == c: answer *= a**3 + b**3 + c**3
    return answer

# Best solution
def solution(a, b, c):
    check = len(set([a,b,c]))
    if check == 1: return 3*a*3*(a**2)*3*(a**3)
    elif check == 2: return sum([a,b,c])*(a**2+b**2+c**2)
    else: return sum([a,b,c])