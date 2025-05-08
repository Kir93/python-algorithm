# ad 제거하기
def solution(strArr):
    answer = []
    for x in strArr:
        if 'ad' not in x: answer.append(x)
    return answer

# for문 if else가 아니라 if 사용 시 if문 for 문 뒤에 작성
def solution(strArr):
    return [word for word in strArr if 'ad' not in word]