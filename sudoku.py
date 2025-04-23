def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty

    for num in range(1, 10):  # Numbers 1-9
        if is_safe(board, row, col, num):
            board.grid[row][col] = num

            if solve_sudoku(board):
                return True

            board.grid[row][col] = 0  # Reset on backtrack

    return False  # Trigger backtrack

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board.grid[i][j] == 0:
                return (i, j)
    return None

def is_safe(board, row, col, num):
    # Check if num is not in the given row, column and 3x3 box
    for x in range(9):
        if board.grid[row][x] == num or board.grid[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board.grid[i + start_row][j + start_col] == num:
                return False

    return True

class Board:
    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        board_str = ""
        for row in self.grid:
            board_str += " ".join(str(num) if num != 0 else '.' for num in row) + "\n"
        return board_str

# You can add utility functions here if needed

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    board = Board(puzzle)
    if solve_sudoku(board):
        print("Sudoku solved!")
        print(board)
    else:
        print("No solution exists.")
