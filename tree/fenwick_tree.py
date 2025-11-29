# Fenwick Tree can get range sum in log(n) time for mutable input array
# https://leetcode.com/problems/range-sum-query-mutable/
class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        """a[i] += delta"""
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
        """prefix sum [0..i]，i < 0 returns 0"""
        if i < 0:
            return 0
        i += 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def range_sum(self, l: int, r: int) -> int:
        """sum over [l..r]"""
        return self.sum(r) - self.sum(l - 1)
