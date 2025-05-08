# 옹알이(1)
def solution(babbling):
    babyWord = ["aya", "ye", "woo", "ma"]
    answer = 0
    for x in babbling:
        for w in babyWord:
            if w in x: x = x.replace(w, '*')
            
        if len(x) == x.count('*'): answer += 1
    return answer

# retry
def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for b in babbling:
        for w in word:
            if w in b: b = b.replace(w, '*')
        if len(b) == b.count('*'): answer += 1
        
    return answer