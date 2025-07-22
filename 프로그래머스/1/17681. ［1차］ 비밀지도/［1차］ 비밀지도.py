def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        combined = format(arr1[i] | arr2[i], f'0{n}b')
        answer.append(''.join('#' if c == '1' else ' ' for c in combined))
        
    return answer

# format(x, f'0{n}b')로 자릿수 원하는 방식으로 맞출 수 있음.
# |로 2진수 변환 없이 bit or 연산 가능