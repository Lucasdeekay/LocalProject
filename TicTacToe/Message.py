# Method prints game instructions
def print_instruction():
    message = "\nTo play Tic-Tac-Toe, input the right index of the desired position\n" \
              "Index are shown below alongside diagram of the game board\n" \
              "\n" \
              "|0|1|2|\n" \
              "|3|4|5|\n" \
              "|6|7|8|\n" \
              "\n" \
              "Input the desired index to insert your avatar into the desired position\n"
    print(message)


# Method prints score
def print_scoreline(score_list, player_list):
    scoreline = "\n" \
                f"{player_list[0]} -> {score_list[0]}\n" \
                f"{player_list[1]} -> {score_list[1]}\n"
    print(scoreline)

