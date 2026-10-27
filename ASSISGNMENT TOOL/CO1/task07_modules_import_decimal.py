# Task 7 - Modules and Import Statements
from decimal import Decimal

quantity = Decimal(input("Enter milk quantity in litres: "))
rate = Decimal(input("Enter rate per litre (Rs.): "))

payment = quantity * rate
print(f"Total payment: Rs. {payment:.2f}")
