def get_valid_moves(board):
    validMoves = []

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == 0 or cell == -1:
                continue

            if x + 2 <= len(board) - 1 and board[x + 1][y] == 1 and board[x + 2][y] == 0:
                validMoves.append(([x, y], [x + 1, y], [x + 2, y]))
            if x - 2 >= 0 and board[x - 1][y] == 1 and board[x - 2][y] == 0:
                validMoves.append(([x, y], [x - 1, y], [x - 2, y]))
            if y + 2 <= len(board) - 1 and board[x][y + 1] == 1 and board[x][y + 2] == 0:
                validMoves.append(([x, y], [x, y + 1], [x, y + 2]))
            if y - 2 >= 0 and board[x][y - 1] == 1 and board[x][y - 2] == 0:
                validMoves.append(([x, y], [x, y - 1], [x, y - 2]))

    return validMoves


def perform_move(board, move):
    board_state_after_move = [0, 0, 1]
    for index, [x, y] in enumerate(move):
        board[x][y] = board_state_after_move[index]


def get_heuristic(board):
    heuristic = 0
    for row in board:
        for cell in row:
            if cell == 1:
                heuristic += 1
    return heuristic


def print_board(board):
    for row in board:
        row_as_string = ""
        for cell in row:
            if cell == 1:
                row_as_string += " 1 "
            elif cell == 0:
                row_as_string += " 0 "
            else:
                row_as_string += "   "
        print(row_as_string)
    print("\n")
