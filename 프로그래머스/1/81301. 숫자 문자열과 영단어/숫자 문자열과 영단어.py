numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
    for i, num in enumerate(numbers):
        s = s.replace(num, str(i))

    return int(s)