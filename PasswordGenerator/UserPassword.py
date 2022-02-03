# Program allows user to change password
from PasswordGenerator import GenerateUniquePassword


def change_password():
    password_list = GenerateUniquePassword.generate_password_list()
    password = "".join(password_list)
    print(f"Password: {password}\n")

    while True:
        confirm_password = int(input("Enter\n1 -> Yes\n2 -> No\n\nDo you want to change password? "))
        if confirm_password == 1:
            password = input("\nEnter Password: ")
            print("Password Successfully Changed!\n")
            break

        elif confirm_password == 2:
            print("\n")
            break

        else:
            print("Invalid Input\n")

    print(f"Password: {password}")


change_password()
