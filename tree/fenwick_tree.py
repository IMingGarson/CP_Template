class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_query(self, start, end):
        return self.prefix_sum(end) - self.prefix_sum(start - 1)
