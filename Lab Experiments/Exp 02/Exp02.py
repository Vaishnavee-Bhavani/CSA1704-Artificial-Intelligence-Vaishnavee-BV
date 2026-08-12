def solve_n_queens(n=8):
    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(list(board))
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)
    return solutions

# Test Run
solutions = solve_n_queens(8)
print("--- 8-Queens Problem ---")
print(f"Total solutions found: {len(solutions)}")
print("\nFirst Solution Matrix:")
first_sol = solutions[0]
for r in range(8):
    row_str = " ".join("Q" if first_sol[r] == c else "." for c in range(8))
    print(row_str)
