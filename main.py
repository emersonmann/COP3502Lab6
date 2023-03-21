"""
Emerson Mann
"""



def encode(password): # define function
    encoded = '' # create empty string
    for i in range(8): # iterate
        encoded += str(int(password[i])+3) # add 3 to each element in password then convert back to string
    return encoded


def decode(encoded): # define function
    decoded = '' # create an empty string
    for i in range(8):
        decoded += str(int(encoded[i]) - 3) # subtract 3 from each
    return decoded


def main():

    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option = int(input('Please enter an option: '))

        if option == 1:
            password = (input('Please enter your password to encode: '))
            encoded_pass = encode(password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            decoded_pass = decode(encoded_pass)
            print('The encoded password is' + encoded_pass + ', and the original password is' + decoded_pass + '.')
        elif option == 3:
            break


if __name__ == '__main__':
    main()

