import string
import random

def password_generator():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))

    # All possible characters including lower case, upper case, digits and special characters
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Use a combination of random characters to generate a password of the specified length
    password = "".join(random.choice(all_characters) for _ in range(length))

    # Display the Password: Print the generated password on the screen
    print("Your generated password is: ", password)

password_generator()
