from collections import deque

def water_jug_problem(cap_a, cap_b, target):
    queue = deque([(0, 0, [])])  # (jug1, jug2, path)
    visited = set()

    while queue:
        j1, j2, path = queue.popleft()

        if j1 == target or j2 == target:
            return path + [(j1, j2)]

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        possible_moves = [
            (cap_a, j2),  # Fill Jug 1
            (j1, cap_b),  # Fill Jug 2
            (0, j2),      # Empty Jug 1
            (j1, 0),      # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (j1 - min(j1, cap_b - j2), j2 + min(j1, cap_b - j2)),
            # Pour Jug 2 -> Jug 1
            (j1 + min(j2, cap_a - j1), j2 - min(j2, cap_a - j1))
        ]

        for move in possible_moves:
            if move not in visited:
                queue.append((move[0], move[1], path + [(j1, j2)]))

    return None

# Test Run (4L and 3L jugs to get 2L)
steps = water_jug_problem(4, 3, 2)
print("--- Water Jug Problem Solution Steps ---")
for step, (j1, j2) in enumerate(steps):
    print(f"Step {step}: Jug A = {j1}L, Jug B = {j2}L")
