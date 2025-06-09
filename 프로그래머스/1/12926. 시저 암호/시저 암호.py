def solution(s, n):
    answer = []
    
    for w in s:
        if w == ' ': answer.append(w)
        else:
            convert_w = ord(w) + n
            
            if (ord(w) <= 90 and convert_w > 90) or (ord(w) <= 122 and convert_w > 122):
                convert_w -= 26
            
            answer.append(chr(convert_w))
            
    return ''.join(answer)