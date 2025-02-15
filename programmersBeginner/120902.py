# 문자열 계산하기
def solution(my_string):
    numbers = []
    operators = []
    
    for x in my_string.split():
        if x.isdigit(): numbers.append(int(x))
        else: operators.append(x)
    
    answer = numbers.pop(0)
    
    while numbers:
        operator = operators.pop(0)
        number = numbers.pop(0)
        if operator == '+': answer += number
        else: answer -= number
        
    return answer

# Best Solution
def solution(my_string):
    return sum(int(x) for x in my_string.replace(' - ', ' + -').split(' + '))