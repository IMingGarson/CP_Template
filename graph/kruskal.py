# https://leetcode.com/problems/min-cost-to-connect-all-points/
def kruskal(graph, n):
    edges = []
    for u in range(n):
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    edges.sort()

    mst_edges = []
    ds = DisjointSet(n) # use disjoint set to group edges
    for edge in edges:
        weight, u, v = edge
        if ds.union(u, v):
            mst_edges.append((u, v, weight))

    return mst_edges
