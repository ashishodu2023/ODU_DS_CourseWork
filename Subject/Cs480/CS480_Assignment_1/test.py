from collections import deque

def is_valid_move(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0])

def print_board(board):
    for row in board:
        print("".join(row))
    print()

def find_neighbors(board, pos):
    neighbors = []
    x, y = pos
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(board, new_x, new_y) and board[new_x][new_y] != '#':
            neighbors.append((new_x, new_y))
    return neighbors

def bfs_robot_push_pull(board, robot, boxes, targets):
    start_state = (robot, boxes)
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        (robot, boxes), actions = queue.popleft()

        if sorted(boxes) == sorted(targets):
            return actions

        if (robot, boxes) in visited:
            continue

        visited.add((robot, boxes))

        solution_board = [list(row) for row in board]
        for box in boxes:
            x, y = box
            solution_board[x][y] = 'B'
        solution_board[robot[0]][robot[1]] = 'R'
        print_board(solution_board)

        for neighbor in find_neighbors(board, robot):
            new_robot = neighbor
            new_boxes = list(boxes)
            for i, box in enumerate(new_boxes):
                if box == new_robot:
                    new_box = (box[0] + (box[0] - robot[0]), box[1] + (box[1] - robot[1]))
                    if is_valid_move(board, *new_box) and board[new_box[0]][new_box[1]] != '#':
                        new_boxes[i] = new_box
                        break

            new_state = (new_robot, tuple(new_boxes))
            new_actions = actions + [neighbor]
            queue.append((new_state, new_actions))

    return None

# Define the game board
board = [
    "##########",
    "#        #",
    "# T BR   #",
    "#        #",
    "#        #",
    "#        #",
    "##########",
]

# Find the robot, boxes, and target positions
targets = {(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == 'T'}
robot = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == 'R'][0]
boxes = tuple((x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == 'B')

actions = bfs_robot_push_pull(board, robot, boxes, targets)

if actions:
    print("Solution found:")
    solution_board = [list(row) for row in board]
    for action in actions:
        x, y = action
        solution_board[x][y] = 'R'
    print_board(solution_board)
else:
    print("No solution found.")
