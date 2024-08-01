class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.cols * 2 - 1))

    def is_valid_move(self, col):
        return self.board[0][col] == ' '

    def make_move(self, col, player):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = player
                return

    def check_winner(self, player):
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True

        for col in range(self.cols):
            for row in range(self.rows - 3):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True

        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True

        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True

        return False

    def is_full(self):
        return all(self.board[0][col] != ' ' for col in range(self.cols))

    def evaluate_window(self, window, player, opponent):
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

    def evaluate_board(self, player):
        opponent = 'X' if player == 'O' else 'O'
        score = 0

        # Evaluate rows, columns, and diagonals
        for r in range(self.rows):
            for c in range(self.cols - 3):
                window = [self.board[r][c + i] for i in range(4)]
                score += self.evaluate_window(window, player, opponent)

            for c in range(self.cols):
                window = [self.board[r + i][c] for i in range(4)]
                score += self.evaluate_window(window, player, opponent)

        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                window = [self.board[r + i][c + i] for i in range(4)]
                score += self.evaluate_window(window, player, opponent)

                window = [self.board[r + 3 - i][c + i] for i in range(4)]
                score += self.evaluate_window(window, player, opponent)

        return score

    def minimax(self, depth, alpha, beta, maximizing_player):
        score = self.evaluate_board('X')  # Evaluate from the perspective of the AI

        if score == 100 or score == -100 or depth == 0:
            return score

        if maximizing_player:
            max_eval = float('-inf')
            for col in range(self.cols):
                if self.is_valid_move(col):
                    row = self.find_empty_row(col)
                    self.make_move(col, 'X')
                    eval = self.minimax(depth - 1, alpha, beta, False)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    self.board[row][col] = ' '  # Undo the move
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float('inf')
            for col in range(self.cols):
                if self.is_valid_move(col):
                    row = self.find_empty_row(col)
                    self.make_move(col, 'O')
                    eval = self.minimax(depth - 1, alpha, beta, True)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    self.board[row][col] = ' '  # Undo the move
                    if beta <= alpha:
                        break
            return min_eval

    def find_empty_row(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                return row
        return None

    def best_move(self):
        max_eval = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        best_col = None

        for col in range(self.cols):
            if self.is_valid_move(col):
                row = self.find_empty_row(col)
                self.make_move(col, 'X')
                eval = self.minimax(4, alpha, beta, False)  # Adjust the depth here
                if eval > max_eval:
                    max_eval = eval
                    best_col = col
                alpha = max(alpha, eval)
                self.board[row][col] = ' '  # Undo the move

        return best_col

if __name__ == "__main__":
    connect_four = ConnectFour()

    while True:
        connect_four.print_board()

        # Player's move
        while True:
            try:
                player_col = int(input("Enter your move (0-6): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if 0 <= player_col <= 6 and connect_four.is_valid_move(player_col):
                connect_four.make_move(player_col, 'O')
                if connect_four.check_winner('O'):
                    connect_four.print_board()
                    print("You win!")
                    exit()
                break
            else:
                print("Invalid move. Try again.")

        # Check if the board is full after the player's move
        if connect_four.is_full():
            connect_four.print_board()
            print("It's a tie!")
            exit()

        connect_four.print_board()

        # AI's move
        ai_col = connect_four.best_move()
        connect_four.make_move(ai_col, 'X')
        if connect_four.check_winner('X'):
            connect_four.print_board()
            print("AI wins!")
            exit()

        # Check if the board is full after AI's move
        if connect_four.is_full():
            connect_four.print_board()
            print("It's a tie!")
            exit()
