class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)  # Uncomment this line if it's an undirected graph

    def dfs(self, start_vertex):
        visited = set()

        def dfs_recursive(vertex):
            visited.add(vertex)
            print(vertex, end=' ')

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)

# Example Usage:
# Create a graph
graph = Graph()

# Add vertices
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)

# Add edges
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)

# Perform DFS starting from vertex 0
print("Depth First Search:")
graph.dfs(0)
