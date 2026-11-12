contacts = [
    ("Dr. Ravi", "+91 98400 12345", "ravi@gmail.com"),
    ("ravi kumar", "9840012345", "ravi@yahoo.com"),
    ("RAVI", "+91 98765 43210", "ravi@gmail.com"),
    ("Arun", "9123456789", "arun@gmail.com")
]

merged = {}

for name, phone, email in contacts:
    # Normalize phone number
    number = "".join(filter(str.isdigit, phone))
    if number.startswith("91") and len(number) == 12:
        number = number[2:]

    # Normalize name
    name = name.lower().replace("dr.", "").strip()

    # Merge records with the same normalized phone number
    if number not in merged:
        merged[number] = {
            "name": name,
            "numbers": set(),
            "emails": set()
        }

    merged[number]["numbers"].add(number)
    merged[number]["emails"].add(email)

for number, details in merged.items():
    print("Name:", details["name"])
    print("Numbers:", details["numbers"])
    print("Emails:", details["emails"])
    print()
