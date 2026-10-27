# Task 6 - User-Defined Functions
def calculate_payment(quantity, rate):
    return quantity * rate

quantity = float(input("Enter milk quantity in litres: "))
rate = float(input("Enter rate per litre (Rs.): "))

result = calculate_payment(quantity, rate)
print(f"Total payment: Rs. {result:.2f}")
