class CrosswordSolver:
    def __init__(self, grid, word_data):
        self.grid = grid
        self.word_data = word_data

    def check_horizontal_vertical(self, word, row, col, direction):
        if direction == "across":
            if col + len(word) > len(self.grid[0]):
                return False
            for i in range(len(word)):
                if self.grid[row][col + i] != " " and self.grid[row][col + i] != word[i]:
                    return False
            for i in range(len(word)):
                if self.grid[row][col + i] == "#":
                    return False
        else:  # direction == "down"
            if row + len(word) > len(self.grid):
                return False
            for i in range(len(word)):
                if self.grid[row + i][col] != " " and self.grid[row + i][col] != word[i]:
                    return False
            for i in range(len(word)):
                if self.grid[row + i][col] == "#":
                    return False
        return True

    def set_word(self, word, row, col, direction):
        if direction == "across":
            for i in range(len(word)):
                self.grid[row][col + i] = word[i]
        else:  # direction == "down"
            for i in range(len(word)):
                self.grid[row + i][col] = word[i]

    def get_word(self, word, row, col, direction):
        if direction == "across":
            for i in range(len(word)):
                self.grid[row][col + i] = " "
        else:  # direction == "down"
            for i in range(len(word)):
                self.grid[row + i][col] = " "

    def solve(self):
        if not self.word_data:
            return True

        variable, start_cell, domain = self.word_data[0]
        for row, col in start_cell:
            for word in list(domain):
                if self.check_horizontal_vertical(word, row, col, variable[1:].lower()):
                    self.set_word(word, row, col, variable[1:].lower())
                    domain.remove(word)
                    if self.solve():
                        return True
                    self.get_word(word, row, col, variable[1:].lower())
                    domain.add(word)

        return False

    def solve_and_display(self):
        if self.solve():
            for row in self.grid:
                print("".join(row))
        else:
            print("No solution found")


# Example usage:
crossword_grid = [
    [" ", " ", " ", " ", " "],
    ["#", "#", " ", "#", " "],
    ["#", " ", " ", " ", " "],
    [" ", "#", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", "#", "#", " ", "#"],
]

word_data = [
    ("1ACROSS", [(0, 0)], {"HOSES", "LASER", "SAILS", "SHEET", "STEER"}),
    ("4ACROSS", [(2, 1)], {"HEEL", "HIKE", "KEEL", "KNOT", "LINE"}),
    ("7ACROSS", [(3, 2)], {"AFT", "ALE", "EEL", "LEE", "TIE"}),
    ("8ACROSS", [(4, 0)], {"HOSES", "LASER", "SAILS", "SHEET", "STEER"}),
    ("2DOWN", [(0, 2)], {"HOSES", "LASER", "SAILS", "SHEET", "STEER"}),
    ("3DOWN", [(0, 4)], {"HOSES", "LASER", "SAILS", "SHEET", "STEER"}),
    ("5DOWN", [(2, 3)], {"HEEL", "HIKE", "KEEL", "KNOT", "LINE"}),
    ("6DOWN", [(3, 0)], {"AFT", "ALE", "EEL", "LEE", "TIE"}),
]

solver = CrosswordSolver(crossword_grid, word_data)
solver.solve_and_display()
