def floyd_warshall(graph):
    V = len(graph)
    dist = [[float("inf")] * V for _ in range(V)]

    for i in range(V):
        dist[i][i] = 0

    for i in range(V):
        for j in range(V):
            if graph[i][j] != INF:
                dist[i][j] = graph[i][j]

    # Main algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
