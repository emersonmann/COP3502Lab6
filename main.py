"""
Emerson Mann
"""
def main():


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


if __name__ == '__main__':
    main()

