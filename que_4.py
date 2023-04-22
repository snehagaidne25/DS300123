def count_trees_in_forest(n, edges):
    graph = {i: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    visited = set()
    count = 0
    for node in range(n):
        if node not in visited:
            count += 1
            dfs(graph, node, visited)

    return count

# Example Usage
edges = [(0, 1), (0, 2), (3, 4)]
print(count_trees_in_forest(5, edges))