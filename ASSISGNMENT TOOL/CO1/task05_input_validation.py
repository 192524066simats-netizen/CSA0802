# Task 5 - Input and Validation
try:
    quantity = float(input("Enter milk quantity in litres: "))
    rate = float(input("Enter rate per litre (Rs.): "))

    if quantity < 0 or rate < 0:
        print("Invalid input: quantity and rate cannot be negative.")
    else:
        payment = quantity * rate
        print(f"Total payment: Rs. {payment:.2f}")
except ValueError:
    print("Invalid input: please enter numeric values.")
