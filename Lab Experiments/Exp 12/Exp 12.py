def print_board(b):
    for row in [b[i:i+3] for i in range(0, 9, 3)]:
        print(" | ".join(row))

def check_win(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[i] == b[j] == b[k] == p for i, j, k in wins)

board = [' '] * 9
turn = 'X'
for step in range(9):
    print_board(board)
    move = int(input(f"Player {turn}, enter position (0-8): "))
    if board[move] == ' ':
        board[move] = turn
        if check_win(board, turn):
            print_board(board)
            print(f"Player {turn} wins!")
            break
        turn = 'O' if turn == 'X' else 'X'
    else:
        print("Invalid move!")
