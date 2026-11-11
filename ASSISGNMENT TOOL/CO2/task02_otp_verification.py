# Q2 - Loops and OTP Verification

otp = "1234"
attempts = 0

while attempts < 3:
    entered = input("Enter OTP: ")

    if entered == "":
        continue

    attempts += 1

    if entered == otp:
        print("OTP Verified")
        break

    print("Wrong OTP")
else:
    print("Account Locked")
