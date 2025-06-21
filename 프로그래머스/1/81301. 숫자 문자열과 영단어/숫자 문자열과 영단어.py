numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_dict = {word: str(i) for i, word in enumerate(numbers)}

def solution(s):
    for word, digit in num_dict.items():
        s = s.replace(word, digit)
    return int(s)