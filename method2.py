import math

# Returns an list containing the parsed string
def parse_message(k,message,pad):
    # Append the end of message flag if it is being encrypted, don't if it is being decrypted. 
    if pad == True:
        message += '###'
    parsed_message = []

    # Fill out the message to be a multiple of k, just using 1's here, but the characters could be anything.
    while len(message) % k != 0:
        message += '1'

    # Iterate over the message in multiples of k
    for i in range (0, len(message), k):
        parsed_message.append(message[i:i+k])
    
    return parsed_message


# Returns message block with bits flipped
def flip_bits(C_n,message_chunk):
    ciphertext = []
    
    #print("Chunk TO CIPHER: ", message_chunk)

    for i, char in enumerate(message_chunk):
        binary = ord(char)
        
        # Find the corresponding catalan digit
        digit = int(str(C_n)[i])

        # This bit operation first moves the binary of the digit over four slots, opening up 4 0's, then it performs logical or with itself, filling those 4 0's with a copy of the digit's binary
        doubled_binary = (digit << 4) | digit
        
        binary ^= doubled_binary

        # Rencode the binary
        ciphertext.append(chr(binary))
    #print("CIPHERED CHUNK: ", ciphertext)

    return ''.join(ciphertext) # Concatenate the ciphertext intoa  string

class node():
    def __init__(self,name):
        self.n = 8
        self.name = name
    
    # Used to compute the nth catalan number in the encryption function
    def compute_catalan(self):
        C_n =  math.factorial(2 * self.n) // (math.factorial(self.n + 1) * math.factorial(self.n))
        return C_n

    # N is the nth catalan number to compute
    def encrypt(self,message):
        # Prepare message for encryption
        C_n = self.compute_catalan()       ## Compute catalan number
        number_of_digits = len(str(C_n))    ## Figure out the number of digits that each "Chunk" of the message must be parsed into
        parsed_message = parse_message(number_of_digits,message,True)    ## Parse the message into chunks that are equal to the length of the catalan number. E.g if catalan number is 3 digits long, hello world would be parsed into hel|lo |wor|ld |
        # print("Catalan key", C_n)
        # print("Original message",message)
        #p rint("Parsed message ", parsed_message)

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
        # Compute the agreed upon catalan number
        C_n = self.compute_catalan()
        
        plaintext = []

        # Prase the cipher text out, do not pad with the ###
        parsed_ciphertext = parse_message(len(str(C_n)),message,False)

        # Perform bitswap again, this will undo the ciphering we have done. 
        for chunk in parsed_ciphertext:
            plaintext.append(flip_bits(C_n,chunk))

        # Reconcatenate bit swapped message into a full message
        decrypted_message = ''
        for chunk in plaintext:
            decrypted_message += chunk

        # Slice out everything after the first # sign
        final_index_to_keep = decrypted_message.find('###')
        decrypted_message = decrypted_message[:final_index_to_keep]

        return decrypted_message
    
    # 
    def receive_message(self,message,n_,node):
        self.n = n_
        print( self.name, ' recieved Cipher: ', message, ' from ', node.name)
        message = self.decrypt(message)
        print('Decrypted Message: ', message)
        print()
    
    def send_message(self,message,node,):
        print("Sending message from ",self.name, " to ", node.name)
        to_send = self.encrypt(message)
        node.receive_message(to_send,self.n,self)

n1 = node("Node 1")
n2 = node("Node 2")
n1.n = 30
print(n1.compute_catalan())
n1.send_message("Hello World",n2)