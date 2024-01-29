import random
import string

def GeneratePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def PasswordGenerator():
    print("------------Password Generator----------------")

    while True:
        # Using error handling
        try:
            length = int(input("Enter the length of the password (or enter 'stop' to exit): "))

            if length <= 0:
                print("Please enter a positive length.")
                continue  # Go back to the beginning of the loop

        except ValueError:
            input_value = input("Invalid input. Enter a valid number or 'stop' to exit: ")
            if input_value.lower() == 'stop':
                print("Password Generator stopped.")
                break  # Exit the loop and end the program
            else:
                continue  # Go back to the beginning of the loop if not 'stop'

        password = GeneratePassword(length)
        print(f"Generated Password: {password}")

# Run the password generator
PasswordGenerator()
