# 수 조작하기 1
def solution(n, control):
    for d in control:
        if d == 'w': n += 1
        elif d == 's': n -= 1
        elif d == 'd': n += 10
        else: n -= 10
    return n

# Best solution
def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer