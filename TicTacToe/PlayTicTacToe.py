import random
from TicTacToe import GameBoard, GamePlayer, Message


# Method gets start option
def get_start_option():
    loop = True

    while loop:
        info = "1 -> Start\n" \
               "2 -> Instruction\n" \
               "3 -> Quit"
        print(info)
        try:
            index = int(input("Enter Command: "))
            if 1 <= index <= 3:
                loop = False
                return index

        except ValueError:
            print("Invalid Input\n")


# Method gets game mode
def get_game_mode():
    loop = True
    index = 0

    while loop:
        info = "\n1 -> Win By 1\n" \
               "2 -> Win By 3\n" \
               "3 -> Win By 7"
        print(info)
        try:
            index = int(input("Enter Command: "))
            if 1 <= index <= 3:
                loop = False

        except ValueError:
            print("Invalid Input\n")

    if index == 1:
        return 1
    elif index == 2:
        return 3
    elif index == 3:
        return 7


# Method get player choice of position
def get_player_next_play(board, player_name, player_avatar, current_player):
    loop = True

    print("\n" + current_player)

    if player_name != "Avatar":
        while loop:
            try:
                choice_index = int(input("Enter Position: "))
                board, loop = GameBoard.check_board(board, choice_index, player_name, player_avatar)
            except ValueError:
                print("Invalid Input\n")
    else:
        loop = True
        while loop:
            choice_index = random.randint(0, 8)
            board, loop = GameBoard.check_board(board, choice_index, player_name, player_avatar)

    GameBoard.show_game_board(board)


# Method plays Tic-Tac-Toe
def play_game(players, player_score, game_avatar):
    # Initialize index of current player
    current_player_index = 0

    active = True

    game_board = GameBoard.board_structure()

    print("New Game\n")
    GameBoard.show_game_board(game_board)

    while active:
        current_player = players[current_player_index]
        player_avatar = game_avatar[current_player_index]
        get_player_next_play(game_board, current_player, player_avatar, current_player)
        current_player_index = GamePlayer.switch_players(current_player_index)
        active = GameBoard.check_winner(game_board, player_score, players)

    Message.print_scoreline(player_score, players)


# Main method
def run_tic_tac_toe():
    while True:
        start_option = get_start_option()

        if start_option == 1:
            mode = get_game_mode()
            game_avatar = ['X', 'O']
            players = GamePlayer.get_players()
            player_score = [0, 0]
            while (player_score[0] or player_score[1]) != mode:
                play_game(players, player_score, game_avatar)
            if player_score[0] == mode:
                print(f"\n{players[0]} is the best")
            else:
                print(f"\n{players[1]} is the best")
            break
        elif start_option == 2:
            Message.print_instruction()
        elif start_option == 3:
            print("\nGame Over!!!")
            break


run_tic_tac_toe()
