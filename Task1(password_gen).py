
import random
import string

def generate_password(length, use_digits, use_special_chars):
    # Define character sets
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Check if the character set is empty
    if not characters:
        raise ValueError("Character set is empty. Please select at least one character type.")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password generation options
length = int(input("Enter the password length: "))
use_digits = input("Include digits (yes/no): ").strip().lower() == "yes"
use_special_chars = input("Include special characters (yes/no): ").strip().lower() == "yes"

# Generate and print the password
password = generate_password(length, use_digits, use_special_chars)
print("Generated Password:", password)
