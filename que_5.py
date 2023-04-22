def has_cycle(graph):
    def dfs(node, visited, rec_stack):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    visited = set()
    rec_stack = set()
    for node in graph:
        if node not in visited:
            if dfs(node, visited, rec_stack):
                return True

    return False

# Example Usage
graph = {
    'A': set(['B']),
    'B': set(['C']),
    'C': set(['A'])
}
print(has_cycle(graph)) # True