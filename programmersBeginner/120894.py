# 영어가 싫어요
def solution(numbers):
    convert = {
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
    }
    
    first = ''
    answer = ''
    for s in numbers:
        first += s
        if first in convert:
            answer += str(convert[first])
            first = ''
            
    return int(answer)

# Best Solution
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)