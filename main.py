def encode(base_password):
    base_password = list(base_password)
    encoded_password_list = []
    for i in base_password:
        i = int(i)
        if i == 7:
            i = 0
        if i == 8:
            i = 1
        if i == 9:
            i = 2
        encoded_password_list.append(i + 3)
    encoded_password = ""
    for i in encoded_password_list:
        encoded_password += str(i)
    return encoded_password


def decode(encoded_password):             #Riley's decode function
    decoded = ""
    for i in encoded_password:
        i = int(i)
        if i == 2:
            i = "9"
        elif i == 1:
            i = "8"
        elif i == 0:
            i = "7"
        else:
            i -= 3
            i = str(i)
        decoded += i
    return decoded

if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu_option = int(input("Please enter an option: "))
        if menu_option == 3:
            break
        elif menu_option == 1:
            base_password = input("Please enter your password to encode: ")
            encoded = encode(base_password)
            print("Your password has been encoded and stored!")
        elif menu_option == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")
