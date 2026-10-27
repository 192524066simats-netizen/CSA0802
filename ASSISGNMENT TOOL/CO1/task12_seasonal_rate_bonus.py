# Task 12 - Seasonal Rate and Bonus Calculation
SUMMER_RATE = 40
REGULAR_RATE = 35
ELIGIBLE_BONUS = 20

try:
    quantity = float(input("Enter total milk quantity in litres: "))
    season = input("Enter season (Summer/Regular): ").strip().lower()
    eligible = input("Is farmer eligible for bonus? (yes/no): ").strip().lower()

    if quantity < 0:
        print("Invalid input: quantity cannot be negative.")
    elif season == "summer":
        rate = SUMMER_RATE
        basic_payment = quantity * rate
        bonus = ELIGIBLE_BONUS if eligible == "yes" else 0
        print(f"Seasonal rate: Rs. {rate:.2f}")
        print(f"Basic payment: Rs. {basic_payment:.2f}")
        print(f"Bonus: Rs. {bonus:.2f}")
        print(f"Final payment: Rs. {basic_payment + bonus:.2f}")
    elif season == "regular":
        rate = REGULAR_RATE
        basic_payment = quantity * rate
        bonus = ELIGIBLE_BONUS if eligible == "yes" else 0
        print(f"Seasonal rate: Rs. {rate:.2f}")
        print(f"Basic payment: Rs. {basic_payment:.2f}")
        print(f"Bonus: Rs. {bonus:.2f}")
        print(f"Final payment: Rs. {basic_payment + bonus:.2f}")
    else:
        print("Invalid season. Enter Summer or Regular.")
except ValueError:
    print("Invalid input: enter a valid numeric quantity.")
