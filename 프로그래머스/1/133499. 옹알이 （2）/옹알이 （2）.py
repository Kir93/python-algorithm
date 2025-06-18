def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    answer = 0

    for x in babbling:
        idx = 0
        prev = ''
        is_valid = True

        while idx < len(x):
            matched = False
            
            for word in words:
                if x.startswith(word, idx) and word != prev:
                    prev = word
                    idx += len(word)
                    matched = True
                    break
                    
            if not matched:
                is_valid = False
                break

        if is_valid:
            answer += 1

    return answer