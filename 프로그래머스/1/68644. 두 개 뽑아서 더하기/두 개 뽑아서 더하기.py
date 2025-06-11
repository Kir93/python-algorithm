# import itertools

# def solution(numbers):
#   return sorted(list(set([x + y for x, y in itertools.combinations(numbers, 2)])))

def solution(numbers):
    answer = []
    l = len(numbers)
    
    for i in range(l):
        for j in range(l):
            if i == j: continue
            sum_n = numbers[i] + numbers[j]
            if sum_n not in answer:
                answer.append(sum_n)
    
    return sorted(answer)