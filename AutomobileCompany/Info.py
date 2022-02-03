# Method prints out valid information
def print_information():
    message = "To get started, ENTER\n" \
              "1 => Bicycle\n" \
              "2 => Motorbike\n" \
              "3 => Tricycle\n" \
              "4 => Car\n" \
              "5 => Jeep\n" \
              "6 => Truck\n" \
              "7 => Help/Support\n" \
              "0 => Exit\n"
    print(message)


# Method prints information
def get_help():
    message = "\nContact our support through the following media\n" \
              "E-mail: myautomobilecompany@mail.com\n" \
              "Telephone: +877479763\n"
    print(message)

    return "Exit"


def print_card_or_cash_transaction_details(automobile, price, quantity, discount, gross, net, payment_mode):
    if discount == 0:
        transaction_details = f"\nMode Of Payment => {payment_mode}\n" \
                              f"Automobile => {automobile}\n" \
                              f"Price => #{price}\n" \
                              f"Quantity => {quantity}\n" \
                              f"Total => #{gross}\n" \
                              f"\n" \
                              f"Thank you for your patronage"
    else:
        transaction_details = f"\nMode Of Payment => {payment_mode}\n"\
                              f"Automobile => {automobile}\n" \
                              f"Price => #{price}\n" \
                              f"Quantity => {quantity}\n" \
                              f"Discount => {discount}%\n" \
                              f"Gross Pay => #{gross}\n" \
                              f"Total => #{net}\n" \
                              f"\n" \
                              f"Thank you for your patronage"
    print(transaction_details)


def print_installments_transaction_details(automobile, price, quantity, discount, gross, net, payment_mode, period,
                                           monthly_pay, new_net):
    if discount == 0:
        transaction_details = f"\nMode Of Payment => {payment_mode}\n" \
                              f"Automobile => {automobile}\n" \
                              f"Price => #{price}\n" \
                              f"Quantity => {quantity}\n" \
                              f"Gross Pay => {gross}\n" \
                              f"Duration Of Installments => {period}\n" \
                              f"Monthly Payment => #{monthly_pay}\n" \
                              f"Total => #{new_net}\n" \
                              f"\n" \
                              f"Thank you for your patronage"
    else:
        transaction_details = f"\nMode Of Payment => {payment_mode}\n"\
                              f"Automobile => {automobile}\n" \
                              f"Price => #{price}\n" \
                              f"Quantity => {quantity}\n" \
                              f"Discount => {discount}%\n" \
                              f"Gross Pay => #{gross}\n" \
                              f"Net Pay => #{net}\n" \
                              f"Duration Of Installments => {period}\n" \
                              f"Monthly Payment => #{monthly_pay}\n" \
                              f"Total => #{new_net}\n" \
                              f"\n" \
                              f"Thank you for your patronage"
    print(transaction_details)
