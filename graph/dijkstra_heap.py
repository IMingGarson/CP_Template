# variant with certain conditions
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
def dijkstra(graph, start):
    distances = [float('inf') for _ in range(len(graph))]
    distances[start] = 0
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
