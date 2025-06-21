numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
    answer = []
    convert_num = []

    for num in s:
        if num.isdigit():
            answer.append(num)
        else:
            if numbers.count(str(''.join(convert_num))+num) > 0:
                answer.append(str(numbers.index(''.join(convert_num)+num)))
                convert_num = []
            else:
                convert_num.append(num)

    return int(''.join(answer))