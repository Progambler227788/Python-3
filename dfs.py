# Function of depth first search
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Taking user input to create the graph
def create_graph():
    # graph to hold graph data dictionary
    graph = {}
    vertices = int(input("Enter the number of vertices: "))
    
    for vertex in range(vertices):
        edges = list(map(int, input(f"Enter the vertices adjacent to vertex {vertex}: ").split()))
        graph[vertex] = edges
    
    return graph

# Main function to perform DFS traversal
def main():
    graph = create_graph()
    start_vertex = int(input("Enter the starting vertex for DFS: "))
    print("DFS traversal starting from vertex", start_vertex, ":")
    dfs(graph, start_vertex)

if __name__ == "__main__":
    main()
