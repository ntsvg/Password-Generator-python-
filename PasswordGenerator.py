import random
import string

print("Welcome to the Password Generator!")
print("-------------------------------------------------------------")
print("Creating a strong password is really important to keep your data safe.")
print("Let's create one based on your preferences!\n")

# Ask for password length
while True:
    try:
        length = int(input("Enter the length of the password (min 4): "))
        if length < 4:
            print("Password length should be at least 4.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

print("\nChoose the type of characters for your password:")
print("1. Capital Letters")
print("2. Small Letters")
print("3. Both Capital & Small Letters")
print("4. Digits")
print("5. Special Characters")
print("6. All Characters (Recommended)")

# Asking for a choice
while True:
    try:
        choice = int(input("Enter your choice (1-6): "))
        if choice in range(1, 7):
            break
        else:
            print("Please choose between 1 and 6.")
    except ValueError:
        print("Please enter a valid number.")

# Character selection
if choice == 1:
    characters = string.ascii_uppercase
elif choice == 2:
    characters = string.ascii_lowercase
elif choice == 3:
    characters = string.ascii_letters
elif choice == 4:
    characters = string.digits
elif choice == 5:
    characters = string.punctuation
elif choice == 6:
    characters = string.ascii_letters + string.digits + string.punctuation

# Generating password
password = ''.join(random.choices(characters, k=length))
print("\nYour Strong Password is:", password)
print("Tip: Store it in a password manager for safety!")
print("-------------------------------------------------------------")