import itertools

def travelling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_cost = float('inf')
    best_path = []

    for perm in itertools.permutations(nodes):
        current_cost = 0
        k = start
        valid = True
        for node in perm:
            if node in graph[k]:
                current_cost += graph[k][node]
                k = node
            else:
                valid = False
                break
        if valid and start in graph[k]:
            current_cost += graph[k][start]
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = [start] + list(perm) + [start]

    return best_path, min_cost

tsp_graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}
path, cost = travelling_salesman(tsp_graph, 'A')
print(f"Optimal Path: {path}, Minimum Cost: {cost}")
