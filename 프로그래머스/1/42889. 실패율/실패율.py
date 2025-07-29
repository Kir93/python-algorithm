def solution(N, stages):
    fail_count = [0] * (N + 2)
    for stage in stages:
        fail_count[stage] += 1

    result = []
    total_users = len(stages)
    
    for i in range(1, N + 1):
        fail_rate = fail_count[i] / total_users if total_users > 0 else 0
        result.append((i, fail_rate))
        total_users -= fail_count[i]
    
    result.sort(key=lambda x: x[1], reverse=True)
    
    return [stage for stage, _ in result]