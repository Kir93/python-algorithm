def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    
    for b in babbling:
        prev = ''
        i = 0
        
        while i < len(b):
            found = False
            
            for word in words:
                if b.startswith(word, i) and word != prev:
                    i += len(word)
                    prev = word
                    found = True
                    break

            if not found: break

        if found: answer += 1
            
    return answer