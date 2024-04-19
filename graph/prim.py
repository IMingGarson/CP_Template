# https://leetcode.com/problems/network-delay-time/
# https://leetcode.com/problems/min-cost-to-connect-all-points/

###
# Both Prim's and Kruskal's algorithm are designed to find MST. There are major differences between these two:
# 1. Use cases
#    - Prim's is typically faster for dense graphs, where the number of edges is close to the maximum possible.
#    - Kruskal's is typically faster for sparse graphs, where the number of edges is much less than the maximum possible.
# 2. Implementation
#    - Prim's is generally implemented using a priority queue or a min-heap to efficiently select the next edge to add to the MST.
#    - Kruskal's is implemented using a disjoint-set data structure (union-find) to efficiently detect cycles and maintain the connectivity of the MST.
# 3. Scenario
#    - Prim's is useful when you have a dense graph or when you want to start the MST construction from a "specific vertex".
#    - Kruskal's is useful when you have a sparse graph or when you "don't" have a specific starting vertex in mind for the MST.
#
# In LeetCode contests, both algorithms are typically interchangable, just pay attentation to inputs, constraints and what the problem is asking for.
###


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
        for neighbor_weight, neighbor_node in graph[node]:
            if neighbor_node not in visited:
                heappush(queue, (neighbor_weight + weight, neighbor_node))

return -1
