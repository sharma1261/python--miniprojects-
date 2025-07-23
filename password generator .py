import random

print("Simple Password Generator")

# Step 1: Ask user for length
length = int(input("Enter password length (min 4): "))

# Step 2: Ask user choices
letters_choice = input("Include letters? (yes/no): ")
numbers_choice = input("Include numbers? (yes/no): ")
symbols_choice = input("Include symbols? (yes/no): ")

# Step 3: Define simple sets
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"

# Step 4: Create one string with all selected characters
all_chars = ""

if letters_choice == "yes":
    all_chars += letters
if numbers_choice == "yes":
    all_chars += numbers
if symbols_choice == "yes":
    all_chars += symbols

# Step 5: Validate user has selected at least one set
if all_chars == "":
    print("You must select at least one type of character.")
else:
    password = ""
    count = 0

    # Step 6: Use while loop to generate password
    while count < length:
        password += random.choice(all_chars)
        count += 1

    print("Generated Password:", password)
