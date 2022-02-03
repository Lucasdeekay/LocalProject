# Program generates a random 9-character password

import random
import string


def print_information():
    print("Program generates a random 9-character password\n")


def get_random_inputs(old_list, initialized_list):
    new_list = []
    for loop in range(3):
        new_list.append(random.choice(old_list))
    initialized_list += new_list
    return initialized_list


def generate_password_list():
    generated_password_list = []
    generated_password_list = get_random_inputs(alphabet_list, generated_password_list)
    generated_password_list = get_random_inputs(number_list, generated_password_list)
    generated_password_list = get_random_inputs(symbol_list, generated_password_list)

    shuffled_password_list = []
    for loop in range(len(generated_password_list)):
        pick = random.choice(generated_password_list)

        shuffled_password_list.append(pick)
        generated_password_list.remove(pick)

    return shuffled_password_list


def print_password_string():
    password = "".join(generate_password_list())
    print(f"Password: {password}")


alphabet_list = string.ascii_letters
number_list = string.digits
symbol_list = string.punctuation

print_information()
