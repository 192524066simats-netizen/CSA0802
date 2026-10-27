# Task 9 - Testing and Test Cases
def calculate_payment(quantity, rate):
    if quantity < 0 or rate < 0:
        return "Invalid input"
    return round(quantity * rate, 2)

test_cases = [
    (10, 40, 400),
    (0, 40, 0),
    (5, 30, 150),
    (-5, 40, "Invalid input"),
]

for quantity, rate, expected in test_cases:
    actual = calculate_payment(quantity, rate)
    status = "PASS" if actual == expected else "FAIL"
    print(f"Quantity={quantity}, Rate={rate}, Expected={expected}, Actual={actual} -> {status}")
