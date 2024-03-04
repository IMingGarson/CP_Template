# variant with certain conditions
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

def dijkstra(graph, start):
  # graph = {
  #     0: [(1, 1), (2, 4)],
  #     1: [(0, 1), (2, 2), (3, 5)],
  #     2: [(0, 4), (1, 2), (3, 1)],
  #     3: [(1, 5), (2, 1)]
  # }
  # start_vertex = 0
  distances = [float('inf') for _ in range(len(graph)]
  distances[start] = 0

  pq = [(0, start)]
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
