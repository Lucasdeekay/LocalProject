# Method returns the needed board structure
def board_structure():
    return [
        '_', '_', '_',
        '_', '_', '_',
        '_', '_', '_'
    ]


# Method creates a visual representation of the game board
def show_game_board(board):
    display_board = f"|{board[0]}|{board[1]}|{board[2]}|\n" \
                    f"|{board[3]}|{board[4]}|{board[5]}|\n" \
                    f"|{board[6]}|{board[7]}|{board[8]}|"
    print(display_board)


# Method verifies user choice and inserts players avatar into index chosen
def check_board(board, choice_index, player_name, avatar):
    loop = True
    blank = '_'
    updated_board = board

    if 0 <= choice_index <= 8 and board[choice_index] == blank:
        board[choice_index] = avatar
        loop = False

    elif 0 < choice_index > 8:
        print("Index unavailable\n")

    elif board[choice_index] != blank:
        if player_name != "Avatar":
            print("Position occupied\n")

    return updated_board, loop


# Method checks board for winner or tie
def check_winner(board, score_list, player_list):
    game_on = True
    blank = '_'

    # Player 1
    # Horizontal
    if (board[0] == board[1] == board[2] == 'X') or (board[3] == board[4] == board[5] == 'X') \
            or (board[6] == board[7] == board[8] == 'X'):
        print(f"\n{player_list[0]} wins")
        score_list[0] += 1
        game_on = False
    # Vertical
    elif (board[0] == board[3] == board[6] == 'X') or (board[1] == board[4] == board[7] == 'X') \
            or (board[2] == board[5] == board[8] == 'X'):
        print(f"\n{player_list[0]} wins")
        score_list[0] += 1
        game_on = False
    # Diagonal
    elif (board[0] == board[4] == board[8] == 'X') or (board[2] == board[4] == board[6] == 'X'):
        print(f"\n{player_list[0]} wins")
        score_list[0] += 1
        game_on = False

    # Player 2
    # Horizontal
    elif (board[0] == board[1] == board[2] == 'O') or (board[3] == board[4] == board[5] == 'O') \
            or (board[6] == board[7] == board[8] == 'O'):
        print(f"\n{player_list[1]} wins")
        score_list[1] += 1
        game_on = False
    # Vertical
    elif (board[0] == board[3] == board[6] == 'O') or (board[1] == board[4] == board[7] == 'O') \
            or (board[2] == board[5] == board[8] == 'O'):
        print(f"\n{player_list[1]} wins")
        score_list[1] += 1
        game_on = False
    # Diagonal
    elif (board[0] == board[4] == board[8] == 'O') or (board[2] == board[4] == board[6] == 'O'):
        print(f"\n{player_list[1]} wins")
        score_list[1] += 1
        game_on = False

    elif blank not in board:
        print("\nTie")
        game_on = False

    return game_on
