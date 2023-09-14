import random
import string


def generate_password(length=12):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation


    all_characters = lowercase_letters + uppercase_letters + digits + special_characters


    if length < 6:
        print("Password length must be at least 6 characters.")
        return None

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


def main():
    print("Password Generator")
    print("------------------")

    while True:
        try:
            length = int(input("Enter the desired length for your password: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    password = generate_password(length)

    if password:
        print(f"Generated Password: {password}")
        print("****** THANK YOU *******")


if __name__ == "__main__":
    main()
