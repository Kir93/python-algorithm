import sys

input = sys.stdin.readline

res = []

def divide_and_conquer(histogram, start, end):
    if end == start:
        return histogram[end]
    elif end - start == 1:
        if histogram[end] < histogram[start]:
            return max(2*histogram[end], histogram[start])
        else:
            return max(2*histogram[start], histogram[end])
    
    mid = (start + end) // 2
    left_area = divide_and_conquer(histogram, start, mid)
    right_area = divide_and_conquer(histogram, mid+1, end)
    left = mid-1
    right = mid+1
    mid_area = histogram[mid]
    now_height = histogram[mid]
    while start <= left and right <= end:
        if histogram[left] < histogram[right]:
            if histogram[right] < now_height:
                now_height = histogram[right]
            mid_area = max(mid_area, now_height * (right - left))
            right += 1
        else:
            if histogram[left] < now_height:
                now_height = histogram[left]
            mid_area = max(mid_area, now_height * (right - left))
            left -= 1
            
    while start <= left:
        if histogram[left] < now_height:
            now_height = histogram[left]
        mid_area = max(mid_area, now_height * (right - left))
        left -= 1
    while right <= end:
        if histogram[right] < now_height:
            now_height = histogram[right]
        mid_area = max(mid_area, now_height * (right - left))
        right += 1

    return max(left_area, right_area, mid_area)
        
            
        
res = []
while True:
    histogram = list(map(int, input().split()))
    
    if histogram[0] == 0: break
    
    n = histogram[0]
    
    res.append(divide_and_conquer(histogram, 1, n))

    
for i in res:
    print(i)