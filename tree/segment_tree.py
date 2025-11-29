class LazySegTree:
    """Lazy segment tree supporting range add and range sum."""

    def __init__(self, data: List[int]):
        """Build tree over data[0..n-1]."""
        self.n = len(data)

        size = 1
        while size < self.n:
            size <<= 1
        self.size = size

        self.seg = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

        if self.n:
            self._build(1, 0, self.size, data)

    def _build(self, idx: int, l: int, r: int, data: List[int]) -> None:
        """Internal build on [l, r)."""
        if r - l == 1:
            if l < self.n:
                self.seg[idx] = data[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, data)
        self._build(idx * 2 + 1, m, r, data)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def _apply_lazy(self, idx: int, l: int, r: int, add: int) -> None:
        """Apply lazy add to node covering [l, r)."""
        self.seg[idx] += add * (r - l)
        self.lazy[idx] += add

    def _push(self, idx: int, l: int, r: int) -> None:
        """Push lazy tag at idx to its children."""
        if self.lazy[idx] == 0 or r - l == 1:
            return
        m = (l + r) // 2
        add = self.lazy[idx]
        self._apply_lazy(idx * 2, l, m, add)
        self._apply_lazy(idx * 2 + 1, m, r, add)
        self.lazy[idx] = 0

    def range_add(self, ql: int, qr: int, val: int) -> None:
        """Add val to all positions in [ql, qr)."""
        self._range_add(1, 0, self.size, ql, qr, val)

    def _range_add(self, idx: int, l: int, r: int, ql: int, qr: int, val: int) -> None:
        """Internal range add on [l, r)."""
        if ql >= r or qr <= l:
            return
        if ql <= l and r <= qr:
            self._apply_lazy(idx, l, r, val)
            return
        self._push(idx, l, r)
        m = (l + r) // 2
        self._range_add(idx * 2, l, m, ql, qr, val)
        self._range_add(idx * 2 + 1, m, r, ql, qr, val)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def range_sum(self, ql: int, qr: int) -> int:
        """Return sum on [ql, qr)."""
        return self._range_sum(1, 0, self.size, ql, qr)

    def _range_sum(self, idx: int, l: int, r: int, ql: int, qr: int) -> int:
        """Internal range sum on [l, r)."""
        if ql >= r or qr <= l:
            return 0
        if ql <= l and r <= qr:
            return self.seg[idx]
        self._push(idx, l, r)
        m = (l + r) // 2
        left = self._range_sum(idx * 2, l, m, ql, qr)
        right = self._range_sum(idx * 2 + 1, m, r, ql, qr)
        return left + right
