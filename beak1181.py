import sys
voca_list = []
for i in range(int(sys.stdin.readline())):
# 테스트케이스 수 입력
  voca_list.append(sys.stdin.readline().strip())
  # 입력하는 단어를 리스트로 저장
 
set_voca_list = list(set(voca_list))
# 리스트의 중복 제거
 
sort_voca_list = []
 
for j in set_voca_list:
    sort_voca_list.append((len(j), j))
    # 단어의 길이와 단어를 같이 리스트화 시켜 저장
 
sort_voca_list.sort()
# sort()는 len(j), j 에서 앞을 먼저 정렬후에 앞의 조건이 일치하면 뒤를 정렬한다.
 
for len_voca, voca in sort_voca_list:
  # 리스트를 순환시켜 순서대로 출력
    print(voca)
