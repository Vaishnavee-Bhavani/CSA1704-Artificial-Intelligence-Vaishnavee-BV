def is_valid(node, color, assignment, neighbors):
    for neighbor in neighbors[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(nodes, colors, neighbors, assignment={}):
    if len(assignment) == len(nodes):
        return assignment
    unassigned = [n for n in nodes if n not in assignment][0]
    for color in colors:
        if is_valid(unassigned, color, assignment, neighbors):
            assignment[unassigned] = color
            result = map_coloring(nodes, colors, neighbors, assignment)
            if result:
                return result
            del assignment[unassigned]
    return None

nodes = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
colors = ['Red', 'Green', 'Blue']
neighbors = {
    'WA': ['NT', 'SA'], 'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'], 'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'], 'V': ['SA', 'NSW'], 'T': []
}
print("Map Coloring Solution:", map_coloring(nodes, colors, neighbors))
