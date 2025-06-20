def solution(food):
    p = ''
    for i in range(len(food)):
        if food[i] > 1:
            p += str(i) * (food[i]//2)
    return p + '0' + ''.join(sorted(p, reverse=True))