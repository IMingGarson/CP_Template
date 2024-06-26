# https://leetcode.com/problems/number-of-provinces/
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Fun variant https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/
class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        
    # find parent with path compression
    def find_path_compression(self, x):
        parent = x
        while parent != self.root[parent]:
            self.root[parent] = self.root[self.root[parent]]
            parent = self.root[parent]
        return parent

    # normal find parent
    def find(self, x):
        while node != self.root[node]:
            node = self.root[self.root[node]]
        return node

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return 0
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += self.rank[root_x]
        return 1

    def is_connected(self, x, y):
        return self.root[x] == self.root[y]
