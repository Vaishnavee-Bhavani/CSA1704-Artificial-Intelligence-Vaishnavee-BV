import heapq

class PuzzleState:
    def __init__(self, board, g=0, parent=None):
        self.board = board
        self.g = g  # Cost from start
        self.h = self.calculate_heuristic()  # Manhattan distance
        self.f = self.g + self.h
        self.parent = parent

    def calculate_heuristic(self):
        distance = 0
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        goal_pos = {goal[r][c]: (r, c) for r in range(3) for c in range(3)}
        for r in range(3):
            for c in range(3):
                val = self.board[r][c]
                if val != 0:
                    gr, gc = goal_pos[val]
                    distance += abs(r - gr) + abs(c - gc)
        return distance

    def get_neighbors(self):
        neighbors = []
        r, c = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == 0][0]
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_board = [row[:] for row in self.board]
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                neighbors.append(PuzzleState(new_board, self.g + 1, self))
        return neighbors

    def __lt__(self, other):
        return self.f < other.f

def solve_8_puzzle(initial_board):
    start = PuzzleState(initial_board)
    open_set = [start]
    visited = set()

    while open_set:
        current = heapq.heappop(open_set)
        if current.h == 0:
            path = []
            while current:
                path.append(current.board)
                current = current.parent
            return path[::-1]

        visited.add(str(current.board))
        for neighbor in current.get_neighbors():
            if str(neighbor.board) not in visited:
                heapq.heappush(open_set, neighbor)
    return None

# Test Run
start_board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = solve_8_puzzle(start_board)

print("--- 8-Puzzle Solution ---")
for step, state in enumerate(solution):
    print(f"Step {step}:")
    for row in state:
        print(row)
    print()
