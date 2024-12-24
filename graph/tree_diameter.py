
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/
def tree_diameter(edges):
    if not edges:
        return 0

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        visited = set()
        queue = deque([(start, 0)])  # (node, distance)
        farthest_node = start
        max_distance = 0

        while queue:
            node, distance = queue.popleft()
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
                    if distance + 1 > max_distance:
                        max_distance = distance + 1
                        farthest_node = neighbor

        return farthest_node, max_distance

    start_node = edges[0][0]
    farthest_node, _ = bfs(start_node)
    _, diameter = bfs(farthest_node)

    return diameter

