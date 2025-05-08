def ee(a, b, K):
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while b!= 0: 
        q = a//b
        r = a%b;
        a = b
        b = r
        s = s0 - q*s1
        t = t0 - q*t1
        s0 = s1
        s1 = s
        t0 = t1
        t1 = t
    # (t0 % K + K) % K : t0가 음수 임을 방지
    # if t0 < 0: t0 += K 와 같은 값이다.
    t0 = (t0 % K + K) % K
    # 유클리드 호제법에서 b==0 일 때 a는 gcd
    if a != 1 or t0 > 10**9:
        return 'IMPOSSIBLE'
    return t0

t = int(input())
for i in range(t):
    K, C = map(int, input().split())
    # K, C가 1일 때 예외 처리
    if C == 1:
        if K+1 > 10**9:
            print('IMPOSSIBLE')
        else:
            print(K+1)
        continue
    if K == 1:
        print(1)
        continue
    answer = ee(K, C, K)
    print(answer)