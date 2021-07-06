"""creating the game board"""
game_board = ["_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]


def display_board():
    board = ""
    for n in range(0, 9):
        if n == 2 or n == 5:
            board += game_board[n] + "\n"
        elif n == 8:
            board += game_board[n]
        else:
            board += game_board[n] + " | "
    print(board)


def allocate_piece():
    """allocating pieces to players """
    pieces = ["X", "O"]
    allocate_piece.p1 = input("PLAYER ONE\nSelect a piece. Type X or O: ").upper()
    while allocate_piece.p1 not in pieces:
        print("Invalid Choice\n")
        allocate_piece.p1 = input("PLAYER ONE\nSelect a piece. Type X or O: ").upper()
    if allocate_piece.p1 == "X":
        allocate_piece.p2 = "O"
    else:
        allocate_piece.p2 = "X"


def check_winner():
    if game_board[0] == game_board[1] == game_board[2] == allocate_piece.p1 \
            or game_board[3] == game_board[4] == game_board[5] == allocate_piece.p1 \
            or game_board[6] == game_board[7] == game_board[8] == allocate_piece.p1 \
            or game_board[0] == game_board[3] == game_board[6] == allocate_piece.p1 \
            or game_board[1] == game_board[4] == game_board[7] == allocate_piece.p1 \
            or game_board[2] == game_board[5] == game_board[8] == allocate_piece.p1 \
            or game_board[0] == game_board[4] == game_board[8] == allocate_piece.p1 \
            or game_board[2] == game_board[4] == game_board[6] == allocate_piece.p1:
        return "p1"
    elif game_board[0] == game_board[1] == game_board[2] == allocate_piece.p2 \
            or game_board[3] == game_board[4] == game_board[5] == allocate_piece.p2 \
            or game_board[6] == game_board[7] == game_board[8] == allocate_piece.p2 \
            or game_board[0] == game_board[3] == game_board[6] == allocate_piece.p2 \
            or game_board[1] == game_board[4] == game_board[7] == allocate_piece.p2 \
            or game_board[2] == game_board[5] == game_board[8] == allocate_piece.p2 \
            or game_board[0] == game_board[4] == game_board[8] == allocate_piece.p2 \
            or game_board[2] == game_board[4] == game_board[6] == allocate_piece.p2:
        return "p2"


def handle_turn():
    """getting position where pieces will be placed from the players"""
    p1_score = 0
    p2_score = 0
    turn = 1
    play = True
    while play:
        p1_position = input("Player One Choose a position from 1 to 9: ")
        p1_position = int(p1_position) - 1
        if p1_position > 8 or p1_position < 0:
            print("Invalid Position")
            play = True
        else:
            if game_board[p1_position] == "_":
                game_board[p1_position] = allocate_piece.p1
            else:
                print("Position already taken")
                play = True
        display_board()
        check_p1 = check_winner()
        if check_p1 == "p1":
            p1_score += 1
            print(f"player one {p1_score} : player two {p2_score}")
            play = False
        elif check_p1 != "p1":
            p2_position = input("Player Two Choose a position from 1 to 9: ")
            p2_position = int(p2_position) - 1
            if p2_position > 8 or p2_position < 0:
                print("Invalid Position")
                play = True
            else:
                if game_board[p2_position] == "_":
                    game_board[p2_position] = allocate_piece.p2
                else:
                    print("Position already taken")
                    play = True
            display_board()
            check_p2 = check_winner()
            if check_p2 == "p2":
                p2_score += 1
                print(f"player one {p1_score} : player two {p2_score}")
                play = False
            turn += 1
        if turn == 5:
            print("That's a tie")
            play = False


def start_game():
    display_board()
    allocate_piece()
    handle_turn()


start_game()








