import math

# Returns an list containing the parsed string
def parse_message(k,message):
    # Append the end of message flag
    message += '###'
    parsed_message = []

    # Fill out the message to be a multiple of k, just using 1's here, but the characters could be anything.
    while len(message) % k != 0:
        message += '1'

    # Iterate over the message in multiples of k
    for i in range (0, len(message), k):
        parsed_message.append(message[i:i+k])
    
    return parsed_message

# Figure out which bits to flip
def select_bits_to_flip(C_n,position):
    bits_to_flip = []
    
    # Inkeeping with the method outlined in the literature, we will compute two bits to flip per character of the message. 
    K = int(str(C_n)[position]) # To select a bit we first take a digit in the catalan number
    bit_to_flip1 = K % 8 # The first bit will just be the number mod 8 to fit it into the 8 bit chars that we are encrypting
    bits_to_flip.append(bit_to_flip1)

    bit_to_flip2 = (K + 4) % 8 # The second bit has 4 added to that number and then is modded by 8
    bits_to_flip.append(bit_to_flip2)

    # Return bits_to_flip as the bit indicies that need to be flipped
    return bits_to_flip



    
    pass

# Returns message block with bits flipped
def flip_bits(C_n,k,message_block):
    for chunk in message_block:
        for char in chunk:
            binary = format(ord(char), '08b')  # Extract binary from the char as a string
            indicies_to_flip = bits


class node():
    def __init__(self):
        self.message = ''
    
    def compute_catalan(n):
        C_n =  math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n))
        return C_n



    def encrypt(self,message,n):
        # Prepare message for encryption
        C_n = self.compute_catalan(n)
        number_of_digits = len(str(C_n))
        parsed_message = parse_message(number_of_digits,message)
        
        cipher_text = []
        # Perform bitswap, and generate ciphertext
        for chunk in parse_message:
            cipher_text.append(flip_bits(C_n,number_of_digits,chunk))

        # Reconcatenate into a full message
        encrypted_message = ''
        for chunk in cipher_text:
            encrypted_message += chunk

        return encrypted_message

    def decrypt(self,message):
        return message + ' Decrypted'
    
    def receive_message(self,message):
        self.message = message
        print('Recieved Message: ', self.message)
        self.message = self.decrypt(self.message)
        print('Decrypted Message: ', self.message)
        print()
    
    def send_message(self,message,node):
        to_send = self.encrypt(message)
        node.receive_message(to_send)

# n1 = node()
# n2 = node()

# MESSAGE = 'Combinatorics'

# n1.send_message(MESSAGE,n2)

print(parse_message(3,'message'))
