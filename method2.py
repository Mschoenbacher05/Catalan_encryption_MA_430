import math


class node():
    def __init__(self):
        self.message = ''
    
    def compute_catalan(n):
        C_n =  math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n))
        return C_n

    def encrypt(self,message):
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

n1 = node()
n2 = node()

MESSAGE = 'Combinatorics'

n1.send_message(MESSAGE,n2)
