import sys

def get_z(s):
    z = [0] * len(s)
    z[0] = len(s)

    l, r, k = 0, 0, 0

    for i in range(1, len(s)):
        if i > r:
            l, r = i, i
            while r < len(s) and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < len(s) and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1

    return z

def main():
    input = sys.stdin.readline

    s = input().strip()
    z = get_z(s[::-1])
    num_queries = int(input())
    for _ in range(num_queries):
        i = int(input()) - 1
        print(z[~i])

sys.exit(main())