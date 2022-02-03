# Program shows the workings of a website
from AutomobileCompany import Info
from AutomobileCompany import Calculate
from AutomobileCompany import Process


# Method processes user offer
def collect_user_offer():

    gross_pay = net_pay = discount_given = 0
    loop = True

    price_of_automobile = Process.get_price_of_automobile(automobile_type)
    print(f"Price: #{price_of_automobile}\n")

    while loop:

        quantity_to_be_bought = Process.get_quantity_to_be_purchased()
        stock_availability = Calculate.check_stock(stock_list, automobile_type, quantity_to_be_bought)

        if not stock_availability:

            exit_option = Process.get_exit_option()
            if exit_option == 1:
                print("\nThank you for visiting MyAutomobile.com")
                break

        else:
            Calculate.get_stock_of_automobile(stock_list, automobile_type, quantity_to_be_bought)
            gross_pay = price_of_automobile * quantity_to_be_bought

            if quantity_to_be_bought > 5:
                discount_given = Calculate.get_discount_of_automobile(discount_list, automobile_type)
                net_pay = gross_pay - ((discount_given / 100) * gross_pay)
                print(f"Total Price: #{gross_pay}")
                print(f"Discount: {discount_given}%")
                print(f"Net Total: #{net_pay}\n")
            else:
                print(f"Total Price: #{gross_pay}\n")

        mode_of_payment = Process.get_payment_mode()

        if mode_of_payment == "Card":
            print("\nPlease enter your 4-digit pin")
            Process.get_user_pin()
            Info.print_card_or_cash_transaction_details(automobile_type, price_of_automobile, quantity_to_be_bought,
                                                        discount_given, gross_pay, net_pay, mode_of_payment)
            break

        elif mode_of_payment == "Cash":
            print("\nKindly pay over the counter\n")
            Info.print_card_or_cash_transaction_details(automobile_type, price_of_automobile, quantity_to_be_bought,
                                                        discount_given, gross_pay, net_pay, mode_of_payment)
            break

        elif mode_of_payment == "Installments":
            index_of_duration = Process.get_index_of_duration_of_installments()
            duration = Process.return_duration_of_installment(index_of_duration)
            monthly_payment = Calculate.get_monthly_payments(index_of_duration, gross_pay, net_pay)
            new_net_pay = Calculate.get_total_installments_payment(index_of_duration, monthly_payment)
            Info.print_installments_transaction_details(automobile_type, price_of_automobile, quantity_to_be_bought,
                                                        discount_given, gross_pay, net_pay, mode_of_payment, duration,
                                                        monthly_payment, new_net_pay)
            break


print("Welcome to MyAutomobile.com\n")
goodbye_message = "\nThank you for visiting MyAutomobile.com"

# Initialize lists
stock_list = [50, 50, 50, 50, 50, 50]
discount_list = [6, 9, 10, 12.5, 10, 10]

Info.print_information()

automobile_type = Process.get_automobile_type()

if automobile_type == "Exit":
    print(goodbye_message)
else:
    collect_user_offer()
