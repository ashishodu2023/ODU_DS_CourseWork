import copy

ROWS = 6
COLS = 7

def initialize_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * (COLS * 2 - 1))

def is_valid_move(board, col):
    return board[0][col] == ' '

def make_move(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return

def check_winner(board, player):
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

def is_full(board):
    return all(board[0][col] != ' ' for col in range(COLS))

def evaluate_window(window, player, opponent):
    player_count = window.count(player)
    opponent_count = window.count(opponent)

    if player_count == 4:
        return 100
    elif player_count == 3 and opponent_count == 0:
        return 5
    elif player_count == 2 and opponent_count == 0:
        return 2
    elif opponent_count == 3 and player_count == 0:
        return -4
    elif player_count == 1 and opponent_count == 0:
        return 1
    else:
        return 0

def evaluate_board(board, player):
    opponent = 'X' if player == 'O' else 'O'
    score = 0

    # Evaluate rows
    for row in range(ROWS):
        for col in range(COLS - 3):
            window = [board[row][col + i] for i in range(4)]
            score += evaluate_window(window, player, opponent)

    # Evaluate columns
    for col in range(COLS):
        for row in range(ROWS - 3):
            window = [board[row + i][col] for i in range(4)]
            score += evaluate_window(window, player, opponent)

    # Evaluate diagonals (positive slope)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row + i][col + i] for i in range(4)]
            score += evaluate_window(window, player, opponent)

    # Evaluate diagonals (negative slope)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            window = [board[row - i][col + i] for i in range(4)]
            score += evaluate_window(window, player, opponent)

    return score

def minimax(board, depth, alpha, beta, maximizing_player):
    score = evaluate_board(board, 'X')  # Evaluate from the perspective of the AI

    if score == 100 or score == -100 or depth == 0:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for col in range(COLS):
            if is_valid_move(board, col):
                row = find_empty_row(board, col)
                make_move(board, col, 'X')
                eval = minimax(board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                board[row][col] = ' '  # Undo the move
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for col in range(COLS):
            if is_valid_move(board, col):
                row = find_empty_row(board, col)
                make_move(board, col, 'O')
                eval = minimax(board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                board[row][col] = ' '  # Undo the move
                if beta <= alpha:
                    break
        return min_eval

def find_empty_row(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            return row
    return None

def best_move(board):
    max_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    best_col = None

    for col in range(COLS):
        if is_valid_move(board, col):
            row = find_empty_row(board, col)
            make_move(board, col, 'X')
            eval = minimax(board, 4, alpha, beta, False)  # Adjust the depth here
            if eval > max_eval:
                max_eval = eval
                best_col = col
            alpha = max(alpha, eval)
            board[row][col] = ' '  # Undo the move

    return best_col

if __name__ == "__main__":
    board = initialize_board()

    while True:
        print_board(board)

        # Player's move
        while True:
            try:
                player_col = int(input("Enter your move (0-6): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if 0 <= player_col <= 6 and is_valid_move(board, player_col):
                make_move(board, player_col, 'O')
                if check_winner(board, 'O'):
                    print_board(board)
                    print("You win!")
                    exit()
                break
            else:
                print("Invalid move. Try again.")

        # Check if the board is full after the player's move
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            exit()

        print_board(board)

        # AI's move
        ai_col = best_move(board)
        make_move(board, ai_col, 'X')
        if check_winner(board, 'X'):
            print_board(board)
            print("AI wins!")
            exit()

        # Check if the board is full after AI's move
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            exit()
