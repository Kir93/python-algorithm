def solution(arr, divisor):
    answer = []
    
    for x in arr:
        if x%divisor == 0: answer.append(x)
        
    return sorted(answer) if len(answer) else [-1]