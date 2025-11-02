def calculate_cost( amount_paid, item_cost ):
    change = amount_paid - item_cost
    return round(change, 2) # rounds to 2 decimal places

paid = float(input("Enter how much money you paid: £"))
cost = float(input("Enter how much money you needed to pay: £"))

change = calculate_cost(paid, cost)
print("Your change is: £", change)

