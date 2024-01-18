t = int(input())
for _ in range(t):
    n = int(input())
    parent = [0] * (n + 1) # 각 노드의 부모 저장
    for _ in range(n - 1):
        i, j = map(int, input().split())
        parent[j] = i
    
    a, b = map(int, input().split())
    a_parents, b_parents = [0, a], [0, b] # a와 b가 부모-자식 관계일 수 있으니 인덱스 에러가 나지 않도록 0을 넣어주자
    while parent[a]:
        a_parents.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_parents.append(parent[b])
        b = parent[b]
        
    # 뒤에서부터 거꾸로 탐색하며 가장 가까운 공통 조상을 찾자
    i = 1
    while a_parents[-i] == b_parents[-i]:
        i += 1
        
    print(a_parents[-i + 1])