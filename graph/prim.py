# https://leetcode.com/problems/network-delay-time/
# https://leetcode.com/problems/min-cost-to-connect-all-points/

graph = defaultdict(list)
for u, v, w in times:
    graph[u].append((v, w))

visited = set()
# Prim's algorithm starting at node k
queue = [(0, k)]
res = 0
while queue:
    weight, node = heappop(queue)
    if node not in visited:
        visited.add(node)
        if len(visited) == n:
            return weight
        for neighbor_node, neighbor_weight in graph[node]:
            if neighbor_node not in visited:
                heappush(queue, (neighbor_weight + weight, neighbor_node))

return -1
