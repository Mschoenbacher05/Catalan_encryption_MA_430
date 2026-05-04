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


# Returns message block with bits flipped
def flip_bits(C_n,message_chunk):
    ciphertext = []
    
    #print("Chunk TO CIPHER: ", message_chunk)

    for i, char in enumerate(message_chunk):
        binary = ord(char)
        indices_to_flip = select_bits_to_flip(C_n,i)
        
        # Fact: Python has bit operations. We can use XOR on single bits to flip them:

        ### This creates first a mask that has all 0's but a 1 at the index to flip, then when you xor,if that spot in the binary variable is 1 you would get a 0 back, or if that spot in the binary is a 0, you would get a 1 back
        binary ^= (1 << indices_to_flip[0])  
        binary ^= (1 << indices_to_flip[1])

        # Rencode the binary
        ciphertext.append(chr(binary))
    #print("CIPHERED CHUNK: ", ciphertext)

    return ''.join(ciphertext) # Concatenate the ciphertext intoa  string

class node():
    def __init__(self):
        self.message = ''
    
    # Used to compute the nth catalan number in the encryption function
    def compute_catalan(self,n):
        C_n =  math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
        return C_n

    # N is the nth catalan number to compute
    def encrypt(self,message,n):
        # Prepare message for encryption
        C_n = self.compute_catalan(n)       ## Compute catalan number
        number_of_digits = len(str(C_n))    ## Figure out the number of digits that each "Chunk" of the message must be parsed into
        parsed_message = parse_message(number_of_digits,message)    ## Parse the message into chunks that are equal to the length of the catalan number. E.g if catalan number is 3 digits long, hello world would be parsed into hel|lo |wor|ld |
        print("Catalan key", C_n)
        print("Original message",message)
        print("Parsed message ", parsed_message)

        cipher_text = []
        # Perform bitswap, and generate ciphertext
        for chunk in parsed_message:
            cipher_text.append(flip_bits(C_n,chunk))
            #print("Main CIPHERTEXT: ",cipher_text)

        # Reconcatenate bit swapped message into a full message
        encrypted_message = ''
        for chunk in cipher_text:
            encrypted_message += chunk

        return encrypted_message

    # Decryption step 
    def decrypt(self,message):
        return message + ' Decrypted'
    
    # 
    def receive_message(self,message):
        self.message = message
        print('Recieved Message: ', self.message)
        self.message = self.decrypt(self.message)
        print('Decrypted Message: ', self.message)
        print()
    
    def send_message(self,message,node):
        to_send = self.encrypt(message)
        node.receive_message(to_send)

n1 = node()
print("Encrypted Message",n1.encrypt("Hello world",8))

