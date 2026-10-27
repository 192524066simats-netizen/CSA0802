# Task 4 - Arithmetic Expressions for Payment
quantity = float(input("Enter milk quantity in litres: "))
rate = float(input("Enter rate per litre (Rs.): "))
bonus = float(input("Enter bonus amount (Rs.): "))
deduction = float(input("Enter deduction amount (Rs.): "))

basic_payment = quantity * rate
total_payment = basic_payment + bonus - deduction

print(f"Final payment: Rs. {total_payment:.2f}")
