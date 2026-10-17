def passwordstrength(password):
    isupper = any(char.isupper() for char in password)
    islength = len(password) >= 12
    islower = any(char.islower() for char in password)
    isdigit = any(char.isdigit() for char in password)
    isspecial = any(not char.isalnum() and not char.isspace() for char in password)

    strengthpoint = 5

    print()

    if not isupper:
        strengthpoint -= 1
        print("Try to use some uppercase letters!")

    if not islength:
        strengthpoint -= 1
        print("Try to make it at least 12 characters long!")

    if not islower:
        strengthpoint -= 1
        print("Try to use some lowercase letters!")

    if not isdigit:
        strengthpoint -= 1
        print("Try to use some digits!")

    if not isspecial:
        strengthpoint -= 1
        print("Try to use special characters!")

    common_passwords = [
        "password123",
        "qwerty123",
        "12345678",
        "password",
        "123456",
        "qwerty"
    ]

    if password.lower() in common_passwords:
        strengthpoint = 0
        print("This password is too common! Choose something less predictable.")

    if strengthpoint <= 1:
        thetext = "Very Weak"
    elif strengthpoint == 2:
        thetext = "Weak"
    elif strengthpoint == 3:
        thetext = "Moderate"
    elif strengthpoint == 4:
        thetext = "Strong"
    else:
        thetext = "Very Strong"

    print()
    print(f"Password Strength: {thetext}")
    print(f"Score: {strengthpoint}/5")


def main():
    print("===== PASSWORD STRENGTH CHECKER =====")

    while True:
        password = input("\nEnter your password (or 'exit' to quit): ")

        if password.lower() == "exit":
            print("Goodbye!")
            break

        if len(password) == 0:
            print("Invalid Password: Enter a password!")
            continue

        passwordstrength(password)

        print("====================================")


if __name__ == "__main__":
    main()