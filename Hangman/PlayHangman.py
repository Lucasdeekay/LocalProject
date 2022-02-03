from Hangman import HangmanDisplay
from Hangman import HangmanList


def get_user_guess(all_options):
    while True:
        user_guess = input("Guess: ").upper()
        if user_guess in all_options:
            break
        else:
            print("Invalid Guess\n")

    return user_guess


def verify_user_guess(user_guess, correct_option_list):
    if user_guess in correct_option_list:
        print("Touche!!!\n")
        return True
    else:
        print("Incorrect Guess!!!\n")
        return False


def check_game_status(word_string):
    if "_" not in word_string:
        return True
    else:
        return False


guesses_left = 3
display_index = 0

category = HangmanList.get_category()
secret_word = HangmanList.get_secret_word(category)
secret_word_list = list(secret_word)
secret_word_set = set(secret_word_list)
correct_options = HangmanList.get_correct_options(secret_word_set)
wrong_options = HangmanList.get_wrong_options(correct_options)
options_list = HangmanList.get_shuffled_options_list(correct_options, wrong_options)
secret_word_string = HangmanList.get_display_string(secret_word_list)

while guesses_left > 0:
    display_string = "".join(secret_word_string)
    display = f"CATEGORY: {category}\n" \
              f"SECRET WORD: {display_string}\n" \
              f"OPTIONS: " + "|".join(options_list) + "\n" \
              f"GUESSES LEFT: {guesses_left}"
    print(display)
    guess = get_user_guess(options_list)
    right_guess = verify_user_guess(guess, correct_options)
    options_list.remove(guess)
    if right_guess:
        for index, character in enumerate(secret_word_list):
            if character == guess:
                secret_word_string[index] = character
    else:
        guesses_left -= 1
        display_index += 1

    game_status = check_game_status(secret_word_string)
    if game_status:
        print("You Win")
        HangmanDisplay.display_winner_string()
        break
    elif guesses_left == 0:
        print("Game Over")

    HangmanDisplay.display_loser_string(display_index)
