import random
from pprint import pprint

def is_valid_move(board, row, col, color):
    if board[row][col] != 0:
        return False
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    opposite_color = 1 if color == "black" else 2
    
    valid = False
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if not (0 <= r < len(board) and 0 <= c < len(board[0])):
            continue
        if board[r][c] == opposite_color:
            while 0 <= r < len(board) and 0 <= c < len(board[0]):
                if board[r][c] == 0:
                    break
                if board[r][c] == color:
                    valid = True
                    break
                r, c = r + dr, c + dc
    return valid

def get_valid_moves(board, color):
    valid_moves = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            if is_valid_move(board, r, c, color):
                valid_moves.append((r, c))
    return valid_moves

def select_next_play_random(board, color):
    valid_moves = get_valid_moves(board, color)
    return random.choice(valid_moves)

def select_next_play_ai(board, color):
    valid_moves = get_valid_moves(board, color)
    return valid_moves[0] if valid_moves else None

def select_next_play_human(board, color):
    valid_moves = get_valid_moves(board, color)
    while True:
        try:
            row = int(input("Select a row: "))
            col = int(input("Select a column: "))
            if (row, col) in valid_moves:
                return (row, col)
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")

def set_up_board(width, height):
    board = [[0] * width for _ in range(height)]
    mid_row = height // 2
    mid_col = width // 2
    board[mid_row][mid_col] = 1
    board[mid_row - 1][mid_col - 1] = 1
    board[mid_row][mid_col - 1] = 2
    board[mid_row - 1][mid_col] = 2
    return board

def get_board_as_string(board):
    string_board = ""
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                string_board += "."
            elif board[r][c] == 1:
                string_board += "○"
            elif board[r][c] == 2:
                string_board += "●"
        string_board += "\n"
    return string_board

def human_vs_random():
    board = set_up_board(8, 8)
    player = 1
    while True:
        print(get_board_as_string(board))
        if player == 1:
            move = select_next_play_human(board, "white")
        else:
            move = select_next_play_random(board, "black")
        board[move[0]][move[1]] = player
        player = 3 - player
        if not get_valid_moves(board, "white") and not get_valid_moves(board, "black"):
            break
    print(get_board_as_string(board))
    score = sum(row.count(1) for row in board) - sum(row.count(2) for row in board)
    if score > 0:
        print("Player 1 (White) wins! Score:", score)
        return 1
    elif score < 0:
        print("Player 2 (Black) wins! Score:", -score)
        return 2
    else:
        print("It was a tie")
        return 0

def ai_vs_random():
    board = set_up_board(8, 8)
    player = 1
    while True:
        print(get_board_as_string(board))
        if player == 1:
            move = select_next_play_ai(board, "white")
        else:
            move = select_next_play_random(board, "black")
        if move:
            board[move[0]][move[1]] = player
            player = 3 - player
        if not get_valid_moves(board, "white") and not get_valid_moves(board, "black"):
            break
    print(get_board_as_string(board))
    score = sum(row.count(1) for row in board) - sum(row.count(2) for row in board)
    if score > 0:
        print("Player 1 (White) wins! Score:", score)
        return 1
    elif score < 0:
        print("Player 2 (Black) wins! Score:", -score)
        return 2
    else:
        print("It was a tie")
        return 0

def random_vs_random():
    board = set_up_board(8, 8)
    player = 1
    while True:
        print(get_board_as_string(board))
        move = select_next_play_random(board, "white" if player == 1 else "black")
        board[move[0]][move[1]] = player
        player = 3 - player
        if not get_valid_moves(board, "white") and not get_valid_moves(board, "black"):
            break
    print(get_board_as_string(board))
    score = sum(row.count(1) for row in board) - sum(row.count(2) for row in board)
    if score > 0:
        print("Player 1 (White) wins! Score:", score)
        return 1
    elif score < 0:
        print("Player 2 (Black) wins! Score:", -score)
        return 2
    else:
        print("It was a tie")
        return 0

# Example of usage
result = random_vs_random()
print("Result:", result)
