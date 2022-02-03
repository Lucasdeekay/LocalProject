# Method gets number of players
def get_number_of_players():
    loop = True
    index = 0

    while loop:
        try:
            index = int(input("\nEnter\n"
                              "1 -> One Player\n"
                              "2 -> Two Players\n"
                              "Enter Index: "))
            if 1 <= index <= 2:
                loop = False
            else:
                print("Index unavailable\n")
        except ValueError:
            print("Index must be a number\n")

    return index


# Method gets name of player
def get_player_name(index):
    name = input(f"\nEnter Player {index}: ")
    return name


# Method gets the number and amount of desired players
def get_players():

    players_name_list = []
    number_of_players = get_number_of_players()

    if number_of_players == 2:
        for run in range(2):
            player_name = get_player_name(run+1)
            players_name_list.append(player_name)

    else:
        players_name = get_player_name(1)
        players_name_list.append(players_name)
        # Add default player
        players_name_list.append("Avatar")

    return players_name_list


# Method switch between players
def switch_players(index):
    if index == 0:
        index = 1
    else:
        index = 0

    return index

