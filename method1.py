

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

        # Perform bitswap




        return message + ' Encrypted'  

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
