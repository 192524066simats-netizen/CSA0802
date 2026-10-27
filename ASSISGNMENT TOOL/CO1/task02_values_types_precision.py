# Task 2 - Values, Types and Numerical Precision
quantity = float(input("Enter milk quantity in litres: "))
rate = float(input("Enter rate per litre (Rs.): "))

payment = quantity * rate
print(f"Total payment: Rs. {payment:.2f}")
