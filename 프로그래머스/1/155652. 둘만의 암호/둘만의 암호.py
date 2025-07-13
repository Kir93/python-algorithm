def solution(s, skip, index):
    used = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    mapping = {}
    
    for x in map(chr, range(97, 123)):
        if x in skip:
            continue
        
        i = used.index(x)
        mapping[x] = used[(i + index) % len(used)]
        
    return ''.join(mapping[x] for x in s)