def solution(numbers, hand):
    answer = ''

    pad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }
    
    left = pad['*']
    right = pad['#']
    
    for num in numbers :
        
        if num == 1 or num == 4 or num == 7 :
            answer += 'L'
            left = pad[str(num)]
        elif num == 3 or num == 6 or num == 9 :
            answer += 'R'
            right = pad[str(num)]
        else :
            left_dis = abs(left[0] - pad[str(num)][0]) + abs(left[1] - pad[str(num)][1])
            right_dis = abs(right[0] - pad[str(num)][0]) + abs(right[1] - pad[str(num)][1])
            
            if left_dis < right_dis :
                answer += 'L'
                left = pad[str(num)]
                
            elif left_dis > right_dis :
                answer += 'R'
                right = pad[str(num)]
                
            else :
                if hand == 'right' :
                    answer += 'R'
                    right = pad[str(num)]
                else :
                    answer += 'L'
                    left = pad[str(num)]
    
    return answer