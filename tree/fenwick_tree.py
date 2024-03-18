# Fenwick Tree can get range sum in log(n) time for mutable input array
# https://leetcode.com/problems/range-sum-query-mutable/
class FenwickTree:
    def __init__(self, nums):
        self.size = len(nums)
        self.nums = nums
        self.tree = [0 for _ in range(self.size + 1)]
        for i in range(self.size):
            self.initialize(i, nums[i])

    def initialize(self, index: int, val: int) -> None:
        # binary indexed trees start at index 1
        index += 1
        while index <= self.size:
            self.tree[index] += val
            index += index & -index

    def update(self, index, delta):
        prev_val = self.nums[index]
        self.nums[index] = delta
        index += 1
        while index <= self.size:
            self.tree[index] += delta - prev_val
            index += index & -index

    def prefix_sum(self, index):
        if index < 0:
            return 0
        result = 0
        index += 1
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_query(self, start, end):
        return self.prefix_sum(end) - self.prefix_sum(start - 1)
