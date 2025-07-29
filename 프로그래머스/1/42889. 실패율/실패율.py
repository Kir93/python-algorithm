def solution(N, stages):
    answer = {}
    count = len(stages)
    for i in range(1, N+1):
        answer[i] = stages.count(i) / count if count > 0 else 0
        count -= stages.count(i)

    return sorted(answer, key=lambda x: answer[x], reverse=True)