# Import required modules
import secrets
import string

# Get password length from user
length = int(input("Enter password length: "))

upper = input("Include Uppercase? (y/n): ").lower()
lower = input("Include Lowercase? (y/n): ").lower()
number = input("Include Numbers? (y/n): ").lower()
symbol = input("Include Symbols? (y/n): ").lower()

count = int(input("How many passwords do you want to generate? "))

# Check minimum password length
if length < 8:
    print("Warning: Password should be at least 8 characters long for better security.")

else:
    # Character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Create character pool
    all_characters = ""

    if upper == "y":
        all_characters += uppercase

    if lower == "y":
        all_characters += lowercase

    if number == "y":
        all_characters += digits

    if symbol == "y":
        all_characters += symbols

    # Check if at least one option is selected
    if all_characters == "":
        print("Error: Please select at least one character type.")

    else:
        # Create file and save passwords
        with open("passwords.txt", "w") as file:

            for i in range(count):

                # Generate password
                password = "".join( secrets.choice(all_characters)for j in range(length))

                print(f"\nPassword {i+1}: {password}")
                file.write(f"Password {i+1}: {password}\n")

        # Password Strength Checker
        strength = 0

    if any(char.islower() for char in password): strength += 1

    if any(char.isupper() for char in password): strength += 1

    if any(char.isdigit() for char in password): strength += 1

    if any(char in symbols for char in password): strength += 1

    if length >= 12:
                    strength += 1

        # Display strength
    if strength <= 2:
     print("Password Strength: Weak 🔴")
    elif strength <= 4:
     print("Password Strength: Medium 🟡")
    else:
     print("Password Strength: Strong 🟢")
    print("\n✅ Passwords saved successfully in passwords.txt")