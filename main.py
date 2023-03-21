"""
Emerson Mann
"""
def main():

    def encode(password): # define function
        encoded = '' # create empty string
        for i in range(8): # iterate
            encoded += str(int(password[i])+3) # add 3 to each element in password then convert back to string
        return encoded

if __name__ == '__main__':
    main()

