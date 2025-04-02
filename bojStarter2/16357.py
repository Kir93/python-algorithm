import sys

class SegmentTree():
    __slots__ = ['tree', 'lazy', 'adj', 's', 'e', 'v']

    def __init__(self, n):
        self.adj = 1 << n.bit_length()
        size = self.adj << 1
        self.tree = [0] * size
        self.lazy = [0] * size

    def update_range(self, s, e, v):
        self.s, self.e, self.v = s, e, v
        self._update_range(self.adj, 1, 0, self.adj - 1)

    def _update_range(self, level, node, node_s, node_e):
        next_node1 = node << 1
        next_node2 = next_node1 + 1
        next_level = level >> 1

        if self.lazy[node]:
            self.tree[node] += self.lazy[node]

            if node < self.adj:
                self.lazy[next_node1] += self.lazy[node]
                self.lazy[next_node2] += self.lazy[node]

            self.lazy[node] = 0
        
        if node_e < self.s or node_s > self.e: return
        
        if node_s >= self.s and node_e <= self.e:
            self.tree[node] += self.v
        
            if node < self.adj:
                self.lazy[next_node1] += self.v
                self.lazy[next_node2] += self.v

        else:
            mid = (node_s + node_e) >> 1
            self._update_range(next_level, next_node1, node_s, mid)
            self._update_range(next_level, next_node2, mid + 1, node_e)
            self.tree[node] = self.tree[next_node1] if self.tree[next_node1] > self.tree[next_node2] else self.tree[next_node2]

    def query_range(self, s, e):
        self.s, self.e = s, e
        return self._query_range(self.adj, 1, 0, self.adj - 1)

    def _query_range(self, level, node, node_s, node_e):
        next_node1 = node << 1
        next_node2 = next_node1 + 1
        next_level = level >> 1

        if self.lazy[node]:
            self.tree[node] += self.lazy[node]

            if node < self.adj:
                self.lazy[next_node1] += self.lazy[node]
                self.lazy[next_node2] += self.lazy[node]

            self.lazy[node] = 0
        
        if node_e < self.s or node_s > self.e: return -1 
        if node_s >= self.s and node_e <= self.e: return self.tree[node]
        
        mid = (node_s + node_e) >> 1
        left = self._query_range(next_level, next_node1, node_s, mid)
        right = self._query_range(next_level, next_node2, mid + 1, node_e)

        return left if left > right else right


def main():
    sys.stdin.readline()
    arr1 = sys.stdin.read().splitlines()

    y_set = set()
    arr2 = []
    for a in arr1:
        _, y1, _, y2 = map(int, a.split())
        arr2.append((y1, y2))
        y_set.add(y1); y_set.add(y2)

    transform = {v: i for i, v in enumerate(sorted(y_set))}
    arr2 = [(transform[y1], transform[y2]) for y1, y2 in arr2]

    # 트리에 사각형 전부 채워넣기
    leng = len(transform) - 1
    st = SegmentTree(leng)
    for y1, y2 in arr2:
        st.update_range(y2, y1, 1)

    # 아래에서 위로 이동하며 범위 제거 스위핑
    queue = [(y, is_start, y1, y2) for y1, y2 in arr2 for y, is_start in zip((y2, y1), (True, False))]
    queue.sort(key=lambda x: (x[0], -x[1]))

    amax = 0
    cur_count = 0
    for _, is_start, y1, y2 in queue:
        if is_start:
            cur_count += 1
            st.update_range(y2, y1, -1)

            v = cur_count + st.query_range(y2 + 1, leng)
            if amax < v: amax = v

        else:
            cur_count -= 1

    print(amax)

main()
