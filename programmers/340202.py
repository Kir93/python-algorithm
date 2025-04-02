def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        # usage = total_usage * change[i]/100 --> default
        usage += usage * change[i]/100
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1