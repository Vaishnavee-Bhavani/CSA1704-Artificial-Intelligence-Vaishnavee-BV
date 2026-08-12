from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    traversal_order = []

    visited.add(start_node)

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

# Test Run
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

order = bfs(graph, 'A')
print("--- BFS Traversal Order ---")
print(" -> ".join(order))
