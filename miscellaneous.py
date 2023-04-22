def is_valid(board, row, col, n):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_queens(board, col, n):
    if col == n:
        return True

    for i in range(n):
        if is_valid(board, i, col, n):
            board[i][col] = 1
            if solve_queens(board, col + 1, n):
                return True
            board[i][col] = 0

    return False


def print_board(board):
    for row in board:
        print(row)


def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_queens(board, 0, n):
        print("No solution exists")
    else:
        print_board(board)