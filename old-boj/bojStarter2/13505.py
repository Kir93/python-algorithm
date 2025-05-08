class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, S):
        current_node = self.root
        for s in S:
            if s not in current_node:
                current_node[s] = {}
            current_node = current_node[s]
        current_node[-1] = True

    def search(self, S):
        current_node = self.root
        nums = []
        for s in S:
            if s == 1:
                find = 0
            else:
                find = 1
            if find in current_node:
                nums.append(1)
                current_node = current_node[find]
            else:
                nums.append(0)
                current_node = current_node[s]
        ret = 0
        for i, num in enumerate(nums):
            if num > 0:
                ret += 2 ** (len(S) - i - 1)
        return ret

def main():
    trie = Trie()
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    binaries = []
    maxLen = 0
    for i, num in enumerate(nums):
        temp = (bin(num)[2:])
        nums[i] = temp
        maxLen = max(maxLen, len(temp))
    for i, num in enumerate(nums):
        gap = maxLen - len(num)
        if gap > 0:
            temp = "0" * gap + num
            nums[i] = temp
        temp = list(map(int, nums[i]))
        trie.insert(temp)
        binaries.append(temp)

    answer = 0
    for binary in binaries:
        answer = max(answer, trie.search(binary))
    print(answer)


if __name__ == "__main__":
    main()