import sys
from functools import cmp_to_key
from math import sqrt

input = sys.stdin.readline

# 쿼리를 정렬할 때, 사용되는 대소 비교 함수
def querysort(q1, q2):
    if q1[1] // sqrtN != q2[1] // sqrtN:
        # [s1 / k] < [s2 / k]
        if q1[1] // sqrtN < q2[1] // sqrtN:
            return 1
        else:
            return -1
    else:
        # [s1 / k] = [s2 / k] & e1 < e2
        if q1[2] < q2[2]:
            return 1
        else:
            return -1

    # 버킷 중 위의 두 가지 조건에 처리하는 것을 앞으로 정렬

# 카운트 증가
def Plus(x):
    global res
    if count[x] != 0:
        table[count[x]] -= 1
    count[x] += 1
    table[count[x]] += 1
    res = max(res, count[x])

# 카운트 감소
def Minus(x):
    global res
    table[count[x]] -= 1
    if count[x] == res and table[count[x]] == 0:
        res -= 1
    count[x] -= 1
    table[count[x]] += 1

N = int(input())
V = [0] + list(map(int, input().split()))
sqrtN = sqrt(N)


ans = [0] * 101010 

# count[x] : 구간에 존재하는 x의 개수
count = [0] * 101010 

# table[y] : count[x] == y를 만족하는 y 개수
table = [0] * 101010

# 최댓값
res = 0

query = []
Q = int(input())
for i in range(Q):
    S, E = map(int, input().split())
    query.append((i, S, E))

# 쿼리 정렬 (버킷)
# querysort 함수를 이용해 정렬한다
query = sorted(query, key=cmp_to_key(querysort))

s = 0
e = 0
res = 0

# 투 포인터를 이용해 쿼리 처리
for i in range(Q):
	# 쿼리의 start보다 작은 동안
    while s < query[i][1]:
    	# -> 이므로 빼주어야 한다
        Minus(V[s])
        s += 1
	
    # 쿼리의 start보다 큰 동안
    while s > query[i][1]:
    	# <- 이므로 더해주어야 한다
        s -= 1
        Plus(V[s])
	
    # 쿼리의 end보다 작은 동안
    while e < query[i][2]:
    	# -> 이므로 더해주어야 한다
        e += 1
        Plus(V[e])
	
    # 쿼리의 end보다 큰 동안
    while e > query[i][2]:
    	# <- 이므로 빼주어야 한다.
        Minus(V[e])
        e -= 1
	
    # 쿼리에 대한 결과 저장
    ans[query[i][0]] = res

for i in range(Q):
    print(ans[i])