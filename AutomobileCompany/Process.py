from AutomobileCompany import Info


# Method prompts user and returns an integer value
def get_user_choice_of_automobile():
    user_choice = 0
    loop = True

    while loop:
        try:
            user_choice = int(input("Enter Index Of Automobile: "))
            if user_choice <= 7:
                loop = False
            else:
                print("Index not available\n")
        except ValueError:
            print("Input Must be a Number")

    return user_choice


# Method returns type of automobile
def get_automobile_type():

    index_of_automobile = get_user_choice_of_automobile()

    if index_of_automobile == 0:
        return "Exit"

    elif index_of_automobile == 1:
        return "Bicycle"

    elif index_of_automobile == 2:
        return "Motorbike"

    elif index_of_automobile == 3:
        return "Tricycle"

    elif index_of_automobile == 4:
        return "Car"

    elif index_of_automobile == 5:
        return "Jeep"

    elif index_of_automobile == 6:
        return "Truck"

    elif index_of_automobile == 7:
        return Info.get_help()


# Method returns price of automobile
def get_price_of_automobile(automobile):
    price = 0

    if automobile == "Bicycle":
        price = 10000

    elif automobile == "Motorbike":
        price = 150000

    elif automobile == "Tricycle":
        price = 350000

    elif automobile == "Car":
        price = 550000

    elif automobile == "Jeep":
        price = 750000

    elif automobile == "Truck":
        price = 970000

    return price


# Method collects and returns quantity to be purchased
def get_quantity_to_be_purchased():
    loop = True
    quantity = 0

    while loop:
        try:
            quantity = int(input("Quantity: "))
            loop = False
        except ValueError:
            print("Input must be a number\n")

    return quantity


# Method prompts user
def get_exit_option():

    while True:
        print("Stock available not enough for quantity that wants to be purchased\n"
              "Enter\n"
              "1 => Yes\n"
              "2 => No\n")
        try:
            exit_option = int(input("DO YOU WANT TO EXIT? "))
            if 1 <= exit_option <= 2:
                break
            else:
                print("Index not available\n")
        except ValueError:
            print("Invalid Input\n")

    return exit_option


# Method collects and returns payment mode
def get_payment_mode():

    while True:
        print("Enter\n"
              "1 => Card\n"
              "2 => Cash\n"
              "3 => Installments\n")
        try:
            index_of_mode = int(input("Payment Mode: "))
            if 1 <= index_of_mode <= 3:
                break
            else:
                print("Index not available\n")
        except ValueError:
            print("Invalid Input\n")

    if index_of_mode == 1:
        return "Card"
    elif index_of_mode == 2:
        return "Cash"
    elif index_of_mode == 3:
        return "Installments"


# Method gets user pin for transaction
def get_user_pin():

    while True:
        try:
            pin = int(input("Pin: "))
            if len(str(pin)) == 4:
                break
            else:
                print("Pin must be 4-digits\n")
        except ValueError:
            print("Invalid Input")


# Method prompts user for duration of installments payment
def get_index_of_duration_of_installments():

    while True:
        print("Enter\n"
              "1 => 3months\n"
              "2 => 6months\n"
              "3 => 1year\n")
        try:
            duration = int(input("Enter Index Of Desired Duration: "))
            if 1 <= duration <= 3:
                break
            else:
                print("Index not available\n")
        except ValueError:
            print("Invalid Input")

    return duration


# Method returns duration in string
def return_duration_of_installment(index):
    if index == 1:
        return "3 months"
    elif index == 2:
        return "6 months"
    elif index == 3:
        return "12 months"
