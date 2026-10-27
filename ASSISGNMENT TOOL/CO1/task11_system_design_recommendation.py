# Task 11 - System Design Recommendation
def calculate_payment(quantity, rate):
    if quantity < 0 or rate < 0:
        raise ValueError("Quantity and rate cannot be negative.")
    return quantity * rate

farmer_name = input("Enter farmer name: ")
try:
    quantity = float(input("Enter milk quantity in litres: "))
    rate = float(input("Enter rate per litre (Rs.): "))
    payment = calculate_payment(quantity, rate)

    print("\n--- Payment Details ---")
    print("Farmer:", farmer_name)
    print(f"Quantity: {quantity:.2f} litres")
    print(f"Rate: Rs. {rate:.2f} per litre")
    print(f"Payment: Rs. {payment:.2f}")
except ValueError as error:
    print("Invalid input:", error)
