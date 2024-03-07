# https://leetcode.com/problems/flood-fill/description/
# https://leetcode.com/problems/number-of-islands/
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# Fun variant: https://leetcode.com/problems/island-perimeter/
# depending on where you can go, directions may vary

m, n = len(grid), len(grid[0])
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque([(src_x, src_y)])
while q:
    _x, _y = q.popleft()
    # Some conditions or logics here
    for dx, dy in directions:
        nx, ny = _x + dx, _y + dy
        if 0 <= nx < m and 0 <= ny < n:
            q.append((nx, ny))
