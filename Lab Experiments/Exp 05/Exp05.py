from collections import deque

def is_valid(m, c):
    # Check bounds and safety conditions
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if (m > 0 and m < c) or (3 - m > 0 and (3 - m) < (3 - c)):
        return False
    return True

def solve_missionaries_cannibals():
    # State: (Missionaries on Left, Cannibals on Left, Boat position [1=Left, 0=Right])
    initial_state = (3, 3, 1)
    queue = deque([(initial_state, [])])
    visited = set()

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        (m, c, boat), path = queue.popleft()

        if (m, c, boat) == (0, 0, 0):
            return path + [(0, 0, 0)]

        if (m, c, boat) in visited:
            continue
        visited.add((m, c, boat))

        for dm, dc in moves:
            if boat == 1:  # Boat moving Left to Right
                new_state = (m - dm, c - dc, 0)
            else:          # Boat moving Right to Left
                new_state = (m + dm, c + dc, 1)

            if is_valid(new_state[0], new_state[1]):
                queue.append((new_state, path + [(m, c, boat)]))

# Test Run
path = solve_missionaries_cannibals()
print("--- Missionaries & Cannibals Steps ---")
for step, (m, c, boat) in enumerate(path):
    side = "Left" if boat == 1 else "Right"
    print(f"Step {step}: Left Bank -> Missionaries: {m}, Cannibals: {c} | Boat on {side}")
