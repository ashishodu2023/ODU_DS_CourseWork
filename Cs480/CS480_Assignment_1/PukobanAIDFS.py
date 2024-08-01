

def is_valid_move(board, x, y):
    # Check if the move is within the boundaries of the board
    return 0 <= x < len(board) and 0 <= y < len(board[0])

def PrintBoard(board):
    for row in board:
        print("".join(row))
    print("\n")


def Successor(board, states, xr, yr, path):
    if all(board[x][y] == 'S' for x, y in targets):
        print("Congratulations! You won!")
        return True

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_xr, new_yr = xr + dx, yr + dy
        new_box_x, new_box_y = xr - dx, yr - dy  # Calculate box position for pulling

        if (
            is_valid_move(board, new_xr, new_yr)
            and is_valid_move(board, new_box_x, new_box_y)
            and board[new_xr][new_yr] != '#'
            and (new_xr, new_yr) not in states
        ):
            states.add((new_xr, new_yr))
            states.discard((xr, yr))
            new_board = [list(row) for row in board]
            new_board[xr][yr] = ' '
            new_board[new_xr][new_yr] = 'R'

            if new_board[new_box_x][new_box_y] == 'B':
                new_board[new_box_x][new_box_y] = ' '
                new_board[xr][yr] = 'B'

            path.append(new_board)
            if Successor(new_board, states, new_xr, new_yr, path):
                return True

    return False

# Define the game board
board = [
    "OOOOO",
    "ORBSO",
    "OOOOO",
    "OOOOO"
]

# Find the player and target positions
targets = {(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == 'S'}
xr, yr = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == 'R'][0]

states = {(xr, yr)}
path = [board]

if not Successor(board, states, xr, yr, path):
    print("No solution found.")
else:
    print("Solution path:")
    for step, state in enumerate(path):
        print(f"Step {step}:\n")
        PrintBoard(state)
