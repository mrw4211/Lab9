def encode(base_password):
    base_password = list(base_password)
    encoded_password_list = []
    for i in base_password:
        i = int(i)
        encoded_password_list.append(i + 3)
    encoded_password = ""
    for i in encoded_password_list:
        encoded_password += str(i)
    return encoded_password


def decode(encoded_password):             #Riley's decode function


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
                print("Your password has been encoded and stored!")
            elif menu_option == 2:
