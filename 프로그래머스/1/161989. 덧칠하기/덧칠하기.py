def solution(n, m, section):
    answer = 0
    area = [0] * (n+1)
    i = 0

    while i < len(section):
        start = section[i]
        answer += 1
        painted_end = start + m - 1

        while i < len(section) and section[i] <= painted_end:
            i += 1

    return answer