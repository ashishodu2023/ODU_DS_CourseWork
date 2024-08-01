import heapq
import time

def is_valid_move(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0])

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calculate_heuristic(board, robot, boxes, targets):
    total_dist = 0
    for box in boxes:
        min_dist = min(manhattan_distance(box, target) for target in targets)
        total_dist += min_dist
    return total_dist + manhattan_distance(robot, boxes[0])

def print_board(board):
    for row in board:
        print("".join(row))
    print()

def a_star(board, robot, boxes, targets):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def is_goal(boxes):
        return sorted(boxes) == sorted(targets)

    def apply_move(entity, direction):
        return (entity[0] + direction[0], entity[1] + direction[1])

    def valid_move(entity, direction):
        new_entity = apply_move(entity, direction)
        if not is_valid_move(board, *new_entity) or board[new_entity[0]][new_entity[1]] == '#':
            return False
        return True

    start_state = (robot, tuple(sorted(boxes)))
    visited = set()
    priority_queue = [(0, start_state)]  # (f_cost, (robot, boxes))

    while priority_queue:
        f_cost, (robot, boxes) = heapq.heappop(priority_queue)

        if is_goal(boxes):
            return boxes

        if (robot, boxes) in visited:
            continue

        visited.add((robot, boxes))

        solution_board = [list(row) for row in board]
        for box in boxes:
            x, y = box
            solution_board[x][y] = 'B'
        solution_board[robot[0]][robot[1]] = 'R'
        print_board(solution_board)

        for direction in directions:
            new_robot = apply_move(robot, direction)
            if not is_valid_move(board, *new_robot) or board[new_robot[0]][new_robot[1]] == '#':
                continue

            if (new_robot, boxes) not in visited:
                heapq.heappush(priority_queue, (f_cost + 1 + calculate_heuristic(board, new_robot, boxes, targets),
                                                (new_robot, boxes)))

            for box_index, box in enumerate(boxes):
                if box == new_robot:
                    new_box = apply_move(box, direction)
                    if valid_move(box, direction) and (new_box, boxes[:box_index] + (new_box,) + boxes[box_index + 1:]) not in visited:
                        heapq.heappush(priority_queue, (f_cost + 1 + calculate_heuristic(board, new_robot, boxes, targets),
                                                        (new_robot, boxes[:box_index] + (new_box,) + boxes[box_index + 1:])))
    return None

# Define the game board
board = [
    "##########",
    "#        #",
    "# TP B   #",
    "#  B   B #",
    "#   B R  #",
    "#        #",
    "##########",
]

# Find the robot, boxes, and target positions
targets = {(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == 'T'}
robot = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == 'R'][0]
boxes = tuple((x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == 'B')

result = a_star(board, robot, boxes, targets)

if result:
    print("Solution found:")
    solution_board = [list(row) for row in board]
    for box in result:
        x, y = box
        solution_board[x][y] = 'B'
    print("\n".join(["".join(row) for row in solution_board]))
    print("\n")
    time.sleep(10)
else:
    print("No solution found.")
