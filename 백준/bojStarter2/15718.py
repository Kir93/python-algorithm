def fac(n, P):
    ans = 1
    for i in range(1, n+1):
        ans = (ans*i)%P
    return ans

def com(n, k, P):
    if n < k:
        return 0
    num = (fac(n-k, P) * fac(k, P))%P
    large = pow(num, P - 2, P)
    return (fac(n, P) * large) % P

def C(n, k, P):
    i = 0
    while P ** i <= n:
        i += 1
    i -= 1
    arr1 = []
    arr2 = []

    while True:
        if i == -1:
            break
        arr1.append(n // (P ** i))
        n %= (P ** i)
        arr2.append(k // (P ** i))
        k %= (P ** i)
        i -= 1

    final = 1
    for i in range(len(arr1)):
        final *= com(arr1[i], arr2[i], P)
        final %= P
    return final


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    if N == 0:
        if M == 1:
            print(1)
        else:
            print(0)

    elif M == 1:
        if N != 0:
            print(0)
        else:
            print(1)

    elif  M-1>N:
        print(0)

    else:
        a = C(N-1, M-2, 1031)
        b = C(N-1, M-2, 97)
        m1 = pow(97, 1029, 1031)
        m2 = pow(1031%97, 95, 97)
        ans = a*97*m1 + b*1031*m2
        print(ans%100007)