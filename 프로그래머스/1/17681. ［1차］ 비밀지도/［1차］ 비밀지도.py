def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        bin_arr1 = format(arr1[i], 'b').zfill(n)
        bin_arr2 = format(arr2[i], 'b').zfill(n)
        b = ''
        
        for j in range(n):
            if bin_arr1[j] == '1' or bin_arr2[j] == '1':
                b += '#'
            else:
                b += ' '
        
        answer.append(b)
        
    return answer