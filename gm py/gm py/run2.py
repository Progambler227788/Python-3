import sys

def print_board(board):
    print("  +" + "---+" * len(board[0]))

    col_labels = " ".join(str(i) for i in range(len(board[0])))
    print("    " + col_labels)

    for i, row in enumerate(reversed(board)):
        print("  +" + "---+" * len(row))

        row_data = " ".join(cell.center(3) for cell in row)
        print(str(10 - i).ljust(2) + " | " + row_data + " |")

    print("  +" + "---+" * len(board[0]))


def setup_board(rows, cols):
    board = [[" " for _ in range(cols)] for _ in range(rows)]
    return board

def is_valid_position(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return True
    return False

def is_empty(board, row, col):
    return board[row][col] == " "

def process_setup_input(board, setup_input):
    parts = setup_input.split()
    if len(parts) < 4:
        raise ValueError("Invalid input format")

    object_type = parts[0]
    if object_type not in ['s', 'x', 'd', 'l']:
        raise ValueError(f"Invalid object type {object_type}")

    if object_type == 'x':
        if len(parts) != 4:
            raise ValueError("Invalid input format for blocked field")
        row, col = map(int, parts[1:3])
        if not is_valid_position(board, 9-row, col):
            raise ValueError(f"Field {9-row} {col} not on board")
        board[9-row][col] = 'x'
    elif object_type == 's':
        if len(parts) != 4:
            raise ValueError("Invalid input format for sink")
        size, row, col = map(int, parts[1:])
        if size not in [1, 2]:
            raise ValueError(f"Invalid piece type {size}")
        if not is_valid_position(board, 9-row, col):
            raise ValueError(f"Field {9-row} {col} not on board")
        place_sink(board, 9-row, col, size)
    else:  # Pieces
        if len(parts) != 4:
            raise ValueError("Invalid input format for piece")
        piece_type, row, col = parts[1:]
        row = int(row)
        col = int(col)
        if not is_valid_position(board, 9-row, col):
            raise ValueError(f"Field {9-row} {col} not on board")
        if not is_empty(board, 9-row, col):
            raise ValueError(f"Field {9-row} {col} not free")
        if object_type == 'd':
            board[9-row][col] = piece_type.upper()
        else:
            board[9-row][col] = piece_type.lower()

    return True

def place_sink(board, row, col, size):
    for i in range(row, row + size):
        for j in range(col, col + size):
            board[i][j] = 's'

def perform_move(board, row, col, piece_type):
    if is_valid_position(board, 9-row, col):
        if is_empty(board, 9-row, col):
            board[9-row][col] = piece_type
            return True
        else:
            print(f"ERROR: Field {9-row} {col} is not empty")
            return False
    else:
        print(f"ERROR: Field {9-row} {col} is not on board")
        return False

def check_win_condition(board):
    dark_sinks = 0
    light_sinks = 0
    for row in board:
        for cell in row:
            if cell == 'S':
                dark_sinks += 1
            elif cell == 's':
                light_sinks += 1
    return dark_sinks >= 4 or light_sinks >= 4


def check_lose_condition(board, current_player):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if current_player == "light":
                if cell.lower() == 'l':
                    if (i + 1 < len(board) and is_empty(board, i + 1, j)) or \
                       (i - 1 >= 0 and is_empty(board, i - 1, j)) or \
                       (j + 1 < len(row) and is_empty(board, i, j + 1)) or \
                       (j - 1 >= 0 and is_empty(board, i, j - 1)):
                        return False
            else: 
                if cell.lower() == 'd':
                    if (i + 1 < len(board) and is_empty(board, i + 1, j)) or \
                       (i - 1 >= 0 and is_empty(board, i - 1, j)) or \
                       (j + 1 < len(row) and is_empty(board, i, j + 1)) or \
                       (j - 1 >= 0 and is_empty(board, i, j - 1)):
                        return False
    return True

def main():
    if len(sys.argv) != 4:
        print("ERROR: Too few/too many arguments")
        sys.exit(1)

    try:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
        gui_mode = int(sys.argv[3])
    except ValueError:
        print("ERROR: Illegal argument")
        sys.exit(1)

    if not (8 <= rows <= 10 and 8 <= cols <= 18 and gui_mode in [0, 1]):
        print("ERROR: Illegal argument")
        sys.exit(1)

    board = setup_board(rows, cols)

    print("Initial Board:")
    print_board(board)

    print("Enter setup input (type '#' to finish setup):")
    while True:
        setup_input = input()
        if setup_input == "#":
            break
        try:
            process_setup_input(board, setup_input)
        except ValueError as e:
            print(f"ERROR: {str(e)}")
            sys.exit(1)

        print_board(board)

    print("Enter moves (type '#' to finish moves):")
    current_player = "light"
    while True:
        move_input = input(f"Enter move for {current_player} player (row col piece_type): ")
        if move_input == "#":
            break

        move_parts = move_input.split()
        if len(move_parts) != 3:
            print("ERROR: Invalid move format")
            continue

        try:
            row, col = map(int, move_parts[:2])
            piece_type = move_parts[2]
        except ValueError:
            print("ERROR: Invalid move format")
            continue

        if not is_valid_position(board, 9-row, col):
            print("ERROR: Invalid move. Position out of bounds.")
            continue

        if not perform_move(board, row, col, piece_type):
            continue

        print(f"Move by {current_player} player at ({row}, {col})")
        print_board(board)

        winner = check_win_condition(board)
        if winner:
            print(f"{current_player.capitalize()} player wins!")
            sys.exit(0)

        current_player = "dark" if current_player == "light" else "light"

if __name__ == "__main__":
    main()
