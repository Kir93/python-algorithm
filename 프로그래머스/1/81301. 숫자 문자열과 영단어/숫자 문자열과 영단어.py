numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_dict = {word: str(i) for i, word in enumerate(numbers)}

def solution(s):
    answer = []
    convert_str = []

    for word in s:
        if word.isdigit():
            answer.append(word)
        else:
            convert_str.append(word)
            join_str = ''.join(convert_str)
            if join_str in num_dict:
                answer.append(num_dict[join_str])
                convert_str = []

    return int(''.join(answer))

# def solution(s):
#     for word, digit in num_dict.items():
#         s = s.replace(word, digit)
#     return int(s)