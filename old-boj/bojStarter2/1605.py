import sys
input = sys.stdin.readline

class FixedDoubleRollingHash:
    def __init__(self, seq):
        n = len(seq)

        powers1 = [0] * n
        powers2 = [0] * n
        powers1[0] = powers2[0] = 1
        for i in range(1, n):
            powers1[i] = powers1[i - 1] * 31 % 2147483629
            powers2[i] = powers2[i - 1] * 37 % 2147483647

        hashes1 = [0] * (n + 1)
        hashes2 = [0] * (n + 1)
        for i in range(n):
            hashes1[i + 1] = (hashes1[i] * 31 + seq[i]) % 2147483629
            hashes2[i + 1] = (hashes2[i] * 37 + seq[i]) % 2147483647

        self.hashes1 = hashes1
        self.hashes2 = hashes2
        self.powers1 = powers1
        self.powers2 = powers2

    def hash_range(self, l, r):
        h1 = (self.hashes1[r] - self.hashes1[l] * self.powers1[r - l] % 2147483629) % 2147483629
        h2 = (self.hashes2[r] - self.hashes2[l] * self.powers2[r - l] % 2147483647) % 2147483647
        return h1 << 32 | h2




def main():
    n = int(input())
    s = input().strip()
    arr = [ord(c) - ord("a") for c in s]
    rh = FixedDoubleRollingHash(arr)

    lo = 0
    hi = n

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        seen = set()
        for i in range(n - mid + 1):
            h = rh.hash_range(i, i + mid)
            if h in seen:
                lo = mid
                break
            seen.add(h)
        else:
            hi = mid

    print(lo)


if __name__ == "__main__":
    sys.exit(main())