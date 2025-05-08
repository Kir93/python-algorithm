import sys
from collections import deque
input = sys.stdin.readline
size = 97

class Trie:
    def __init__(self):
        self.top = Node()

    def insert(self, string):
        tmp = self.top
        for k in string:
            key = ord(k)-size
            if not tmp.next[key]:
                tmp.next[key] = Node(key)
            tmp.next[key].parent = tmp
            tmp = tmp.next[key]
        tmp.eos = True

    def trav(self, string):
        tmp = self.top
        for k in string:
            key = ord(k)-size
            if tmp.next[key]:
                tmp = tmp.next[key]
            else:
                while not tmp.next[key]:
                    if tmp == self.top:
                        break
                    tmp = tmp.fail
                if tmp.next[key]:
                    tmp = tmp.next[key]
            if tmp.eos:
                return True
        return False

    def setFail(self):
        qu = deque()
        qu.append(self.top)
        self.top.fail = self.top
        while qu:
            tmp = qu.popleft()
            for nxt in tmp.next:
                if not nxt:
                    continue
                tr = tmp.fail
                if tmp == self.top:
                    nxt.fail = self.top
                    qu.append(nxt)
                    continue
                while not tr.next[nxt.key]:
                    if tr == self.top:
                        break
                    tr = tr.fail
                if tr.next[nxt.key]:
                    nxt.fail = tr.next[nxt.key]
                else:
                    nxt.fail = tr
                if nxt.fail.eos:
                    nxt.eos = True
                qu.append(nxt)


class Node:
    def __init__(self, key=27):
        self.key = key
        self.eos = False
        self.next = [0]*26
        self.fail = None
        self.parent = None


N = int(input().strip())
trie = Trie()
for _ in range(N):
    trie.insert(input().strip())

trie.setFail()
for _ in range(int(input().strip())):
    print("YES" if trie.trav(input().strip()) else "NO")