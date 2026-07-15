# Import required modules
import random
import string

# Get password length from user
length = int(input("Enter password length: "))

# Check minimum password length
if length < 8:
    print("Warning: Password should be at least 8 characters long for better security.")

else:
    # Define characters
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    # Generate password
    password = "".join(random.choice(all_characters) for i in range(length))

    # Display password
    print("\nGenerated Password:", password)

    # Password Strength Checker
    strength = 0

    if any(char.islower() for char in password):
        strength += 1

    if any(char.isupper() for char in password):
        strength += 1

    if any(char.isdigit() for char in password):
        strength += 1

    if any(char in symbols for char in password):
        strength += 1

    if length >= 12:
        strength += 1

    # Display strength
    if strength <= 2:
        print("Password Strength: Weak 🔴")
    elif strength <= 4:
        print("Password Strength: Medium 🟡")
    else:
        print("Password Strength: Strong 🟢")