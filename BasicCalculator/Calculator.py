# Program performs basic calculations
from BasicCalculator import MathsOperations


def print_instruction():
    message = "Input the following to perform operations\n" \
              "+ -> Addition\n" \
              "- -> Subtraction\n" \
              "* -> Multiplication\n" \
              "/ -> Division\n" \
              "^ -> Power\n"
    print(message)


def get_user_number():
    number = 0
    loop = True

    while loop:
        try:
            number = float(input("Enter Number: "))
            loop = False
        except ValueError:
            print("Invalid Input")
    return number


def perform_calculation():

    total = get_user_number()

    operator = ""
    while operator != "=":

        operator = input("Enter Operator: ")

        if operator == "+":
            other_number = get_user_number()
            total =  MathsOperations.add(total, other_number)

        elif operator == "-":
            other_number = get_user_number()
            total = MathsOperations.subtract(total, other_number)

        elif operator == "*":
            other_number = get_user_number()
            total = MathsOperations.multiply(total, other_number)

        elif operator == "/":
            other_number = get_user_number()
            total = MathsOperations.divide(total, other_number)

        elif operator == "^":
            other_number = get_user_number()
            total = MathsOperations.power(total, other_number)

        elif operator == "=":
            result = f"Answer: {total}"
            print(result)

        else:
            print("Invalid Input")


print_instruction()
perform_calculation()
