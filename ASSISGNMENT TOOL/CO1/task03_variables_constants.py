# Task 3 - Variables and Constants
BONUS_RATE = 0  # Fixed bonus amount for this basic example

quantity = float(input("Enter milk quantity in litres: "))
rate = float(input("Enter rate per litre (Rs.): "))

payment = quantity * rate + BONUS_RATE
print(f"Total payment: Rs. {payment:.2f}")
