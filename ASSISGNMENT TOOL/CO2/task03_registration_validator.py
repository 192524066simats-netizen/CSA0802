# Q3 - Vehicle Registration Number Validator

def normalise(text):
    return text.strip().replace(" ", "").replace("-", "").upper()


def validate(reg):
    if len(reg) not in (9, 10):
        return False

    return (
        reg[:2].isalpha()
        and reg[2:4].isdigit()
        and reg[4:-4].isalpha()
        and reg[-4:].isdigit()
    )


reg = input("Enter registration number: ")
reg = normalise(reg)

if validate(reg):
    print("Valid Registration")
    print(reg[:2], reg[2:4], reg[4:-4], reg[-4:])
else:
    print("Invalid Registration")
