import heapq

def a_star(graph, heuristics, start, goal):
    open_list = [(0 + heuristics[start], 0, start, [start])]
    visited = {}

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current == goal:
            return path, g
        if current in visited and visited[current] <= g:
            continue
        visited[current] = g

        for neighbor, weight in graph.get(current, {}).items():
            new_g = g + weight
            new_f = new_g + heuristics.get(neighbor, 0)
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))
            
    return None, float('inf')

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 3},
    'C': {'D': 1, 'E': 2},
    'D': {'G': 3},
    'E': {'G': 1}
}
heuristics = {'A': 4, 'B': 2, 'C': 3, 'D': 2, 'E': 1, 'G': 0}
path, cost = a_star(graph, heuristics, 'A', 'G')
print(f"A* Path: {path}, Cost: {cost}")
