def solution(s, skip, index):
    answer = []
    for x in s:
        ax = ord(x)
        i = index
        while i > 0:
            check_num = ax - 25 if ax + 1 > 122 else ax + 1
            if chr(check_num) not in skip:
                i -= 1
                
            ax = check_num
        
        answer.append(chr(ax))
        
    return ''.join(answer)