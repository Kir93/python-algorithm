# 옹알이(1) - retry
def solution(babbling):
    babyWord = ["aya", "ye", "woo", "ma"]
    answer = 0
    for x in babbling:
        for w in babyWord:
            if w in x: x = x.replace(w, '*')
            
        if len(x) == x.count('*'): answer += 1
    return answer