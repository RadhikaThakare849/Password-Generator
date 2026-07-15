# Import required modules
import random
import string

# Get password length from user
length = int(input("Enter password length:"))

# Check minimum password length
if length < 8:
    print("Warning: Password should be at least 8 characters long for better security.")

# Define letters, digits and symbols
else:
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

# Combine all characters
    all_characters = letters + digits + symbols

# Generate random password
    password = "".join(random.choice(all_characters)for i in range(length))

# Display password
    print("Generated Password:",password)
    