"""
Emerson Mann
"""
def encode(password):
    encoded = ''
    for i in range(8):
        encoded += str(int(password[i])+3)
    return encoded

print(encode('11345682'))


# don't forget comments!!