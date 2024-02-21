import sys

def nearest_neighbor(graph, start):
    num_cities = len(graph)
    visited = [False] * num_cities
    tour = [start]
    total_distance = 0

    visited[start] = True

    for _ in range(num_cities - 1):
        nearest_city = None
        nearest_distance = sys.maxsize
        current_city = tour[-1]

        for neighbor in range(num_cities):
            if not visited[neighbor] and graph[current_city][neighbor] < nearest_distance:
                nearest_city = neighbor
                nearest_distance = graph[current_city][neighbor]

        tour.append(nearest_city)
        visited[nearest_city] = True
        total_distance += nearest_distance

    total_distance += graph[tour[-1]][start]  # Return to starting city
    tour.append(start)

    return tour, total_distance

# Example usage
cities = ["A", "B", "C", "D"]
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_city = 0  # Start from city A

shortest_tour, shortest_distance = nearest_neighbor(distances, start_city)
print("Shortest tour:", shortest_tour)
print("Shortest distance:", shortest_distance)
