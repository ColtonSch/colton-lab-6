def encode_password(password):
    encoded_password = ""
    for char in password:
        if char.isdigit():
            new_digit = (int(char) + 3) % 10
            encoded_password += str(new_digit)
        else:
            encoded_password += char
    return encoded_password

#put the decode password function here

if __name__ == "__main__":
    keep_running = True

    while keep_running == True:
        print("\nPassword Encoder Menu:\n ---------------------")
        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Exit")
        print("\nSelect an option:")
        selection = int(input())

        if selection == 1:
            password = input("Enter your password: ")
            password = encode_password(password)
            print("\nYour password:" + password)

        elif selection == 2:
            print("This is my partner's job")

        elif selection == 3:
            keep_running = False

