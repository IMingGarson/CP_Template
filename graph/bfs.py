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
