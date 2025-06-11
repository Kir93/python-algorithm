import itertools

def solution(numbers):
    return sorted(list(set([x + y for x, y in itertools.combinations(numbers, 2)])))