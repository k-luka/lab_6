# Kirill Luka's file
def main():
    password = ""
    # Loops through menu.
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        # Calls encode function.
        if option == 1:
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        # Calls decode function and prints both passwords.
        elif option == 2:
            print(f"The encoded password is {password}, and the original password is {decode(password)}.\n")
        else:
            break

def encode(password):
    encoded_string = ""
    # Loops through each character of input encoding it.
    for char in password:
        temp = int(char) + 3
        if temp > 9:
            temp -= 10
        encoded_string += str(temp)
    return encoded_string

def decode(password):
    pass

if __name__ == "__main__":
    main()