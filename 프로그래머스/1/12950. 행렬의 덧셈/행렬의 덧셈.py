def solution(arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        sum = []
        for x, y in zip(a1, a2):
            sum.append(x + y)
        answer.append(sum)
    return answer