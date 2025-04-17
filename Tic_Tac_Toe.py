def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:  # Add separator only between rows
            print("-" * (len(row) * 3 - 1))  # Better spacing for the separator

def check_winner(board):
    size = len(board)
    # Check rows
    for row in board:
        if all(cell == row[0] != " " for cell in row):
            return row[0]
    
    # Check columns
    for col in range(size):
        if all(board[row][col] == board[0][col] != " " for row in range(size)):
            return board[0][col]
    
    # Check diagonals
    if all(board[i][i] == board[0][0] != " " for i in range(size)):
        return board[0][0]
    if all(board[i][size-1-i] == board[0][size-1] != " " for i in range(size)):
        return board[0][size-1]
    
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    SIZE = 3
    board = [[" " for _ in range(SIZE)] for _ in range(SIZE)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print(f"Enter row and column numbers (0-{SIZE-1}) separated by space.")
    
    while True:
        print_board(board)
        
        # Get player move
        while True:
            try:
                move = input(f"Player {current_player}'s turn (row col): ").strip()
                row, col = map(int, move.split())
                if not (0 <= row < SIZE and 0 <= col < SIZE):
                    print(f"Numbers must be between 0 and {SIZE-1}.")
                elif board[row][col] != " ":
                    print("That cell is already occupied. Choose another.")
                else:
                    break
            except ValueError:
                print(f"Invalid input. Please enter two numbers (0-{SIZE-1}) separated by space.")
        
        # Make move
        board[row][col] = current_player
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return
        
        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            return
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    while True:
        tic_tac_toe()
        while True:
            replay = input("Do you want to play again? (yes/no): ").strip().lower()
            if replay in ("yes", "no"):
                break
            print("Please enter 'yes' or 'no'.")
        if replay != "yes":
            print("Thanks for playing!")
            break  