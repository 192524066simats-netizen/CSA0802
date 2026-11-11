# Q1 - Conditional Statements

units = int(input("Enter units: "))
ration = input("Ration card (yes/no): ").lower()
age = int(input("Enter age: "))

if units <= 100:
    print("Full Subsidy")
elif units <= 200 and ration == "yes":
    print("Partial Subsidy")
elif units > 200 and age >= 80:
    print("Senior Citizen Exception")
else:
    print("No Subsidy")
