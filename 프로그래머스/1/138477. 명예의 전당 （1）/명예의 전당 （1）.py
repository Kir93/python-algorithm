import heapq

def solution(k, score):
    answer = []
    hall = []
    
    for s in score:
        if len(hall) < k:
            heapq.heappush(hall, s)
        else:
            if s > hall[0]:
                heapq.heappop(hall)
                heapq.heappush(hall, s)
                
        answer.append(hall[0])
        
    return answer