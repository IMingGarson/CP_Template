# https://leetcode.com/problems/sliding-window-maximum/
# To get maximum value within a range, we can use Segment Tree in log(n) time
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, idx, left, right):
        if left == right:
            self.tree[idx] = nums[left]
            return
        mid = (left + right) // 2
        self.build(nums, 2 * idx + 1, left, mid)
        self.build(nums, 2 * idx + 2, mid + 1, right)
        self.tree[idx] = max(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def query(self, idx, left, right, qleft, qright):
        if qleft > right or qright < left:
            return float('-inf')
        if qleft <= left and qright >= right:
            return self.tree[idx]
        mid = (left + right) // 2
        return max(self.query(2 * idx + 1, left, mid, qleft, qright),
                   self.query(2 * idx + 2, mid + 1, right, qleft, qright))

    def maxInRange(self, left, right):
        if left < 0 or right >= self.n or left > right:
            return None  # Handle invalid input
        return self.query(0, 0, self.n - 1, left, right)
