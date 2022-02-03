# Method calculates monthly payment of installments
def get_monthly_payments(duration, gross_pay, net_pay):
    INTEREST_RATE = 0.025
    MONTHS_IN_A_YEAR = 12
    THREE_MONTHS = 3
    SIX_MONTHS = 6

    monthly_payment = 0

    if net_pay > 0:
        interest = net_pay * INTEREST_RATE
        if duration == 1:
            monthly_payment = (net_pay / THREE_MONTHS) + interest
        elif duration == 2:
            monthly_payment = (net_pay / SIX_MONTHS) + interest
        elif duration == 3:
            monthly_payment = (net_pay / MONTHS_IN_A_YEAR) + interest
    else:
        interest = gross_pay * INTEREST_RATE
        if duration == 1:
            monthly_payment = (gross_pay / THREE_MONTHS) + interest
        elif duration == 2:
            monthly_payment = (gross_pay / SIX_MONTHS) + interest
        elif duration == 3:
            monthly_payment = (gross_pay / MONTHS_IN_A_YEAR) + interest

    return monthly_payment


# Method calculates the total balance of installments
def get_total_installments_payment(duration, month_payment):
    MONTHS_IN_A_YEAR = 12
    THREE_MONTHS = 3
    SIX_MONTHS = 6

    total_payment = 0

    if duration == 1:
        total_payment = month_payment * THREE_MONTHS
    elif duration == 2:
        total_payment = month_payment * SIX_MONTHS
    elif duration == 3:
        total_payment = month_payment * MONTHS_IN_A_YEAR

    return total_payment


# Method checks stock of automobile
def check_stock(stock, automobile, quantity):

    status = False
    number = 0

    if automobile == "Bicycle":
        if stock[number] >= quantity:
            status = True

    elif automobile == "Motorbike":
        if stock[number] >= quantity:
            status = True

    elif automobile == "Tricycle":
        if stock[number] >= quantity:
            status = True

    elif automobile == "Car":
        if stock[number] >= quantity:
            status = True

    elif automobile == "Jeep":
        if stock[number] >= quantity:
            status = True

    elif automobile == "Truck":
        if stock[number] >= quantity:
            status = True

    return status


# Method returns current stock of automobile after deducting quantities to be purchased
def get_stock_of_automobile(stock, automobile, quantity):

    if automobile == "Bicycle":
        number = 0
        stock[number] -= quantity

    elif automobile == "Motorbike":
        number = 1
        stock[number] -= quantity

    elif automobile == "Tricycle":
        number = 2
        stock[number] -= quantity

    elif automobile == "Car":
        number = 3
        stock[number] -= quantity

    elif automobile == "Jeep":
        number = 4
        stock[number] -= quantity

    elif automobile == "Truck":
        number = 5
        stock[number] -= quantity


# Method returns discount of automobile
def get_discount_of_automobile(array, automobile):

    number = 0

    if automobile == "Bicycle":
        number = 0

    elif automobile == "Motorbike":
        number = 1

    elif automobile == "Tricycle":
        number = 2

    elif automobile == "Car":
        number = 3

    elif automobile == "Jeep":
        number = 4

    elif automobile == "Truck":
        number = 5

    return array[number]
